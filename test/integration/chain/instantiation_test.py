import os
import sys
import time
import unittest

from hfc.fabric_ca.caservice import ca_service

from hfc.fabric.chain.installment import create_installment_proposal_req
from hfc.fabric.client import Client
from hfc.fabric.msp.msp import msp
from hfc.fabric.peer import Peer
from hfc.fabric.user import User
from hfc.fabric_ca.crypto.crypto import ecies
from hfc.util.keyvaluestore import file_key_value_store
from test.unit.util import cli_call

if sys.version_info < (3, 0):
    from Queue import Queue
else:
    from queue import Queue

CHAINCODE_PATH = 'github.com/example_cc'
CHAINCODE_NAME = 'example_cc'
CHAINCODE_VERSION = 'v1'
CHAIN_ID = 'testchainid1'

USER_ID = 'user'
USER_PASSWD = 'userpw'


def get_submitter():
    ca = ca_service()
    user = User(USER_ID, USER_PASSWD, msp_impl=msp('DEFAULT', ecies()), ca=ca)
    user.enroll()

    return user


class InstantiationTest(unittest.TestCase):
    """ Chaincode related Test cases
    """

    def setUp(self):
        self.gopath_bak = os.environ.get('GOPATH', '')
        gopath = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                               "../../fixtures/chaincode"))
        os.environ['GOPATH'] = os.path.abspath(gopath)
        self.base_path = '/tmp/fabric-sdk-py'
        self.kv_store_path = os.path.join(self.base_path, 'key-value-store')
        self.compose_file_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__),
                         "../../fixtures/chaincode/docker-compose-simple.yml")
        )
        self.start_test_env()

    def tearDown(self):
        if self.gopath_bak:
            os.environ['GOPATH'] = self.gopath_bak
        self.shutdown_test_env()

    def start_test_env(self):
        cli_call(["docker-compose", "-f", self.compose_file_path, "up", "-d"])

    def shutdown_test_env(self):
        cli_call(["docker-compose", "-f", self.compose_file_path, "down"])

    @unittest.skip
    def test_instantiate(self):
        self.shutdown_test_env()
        self.start_test_env()
        time.sleep(5)
        client = Client()
        chain = client.new_chain(CHAIN_ID)
        client.set_state_store(file_key_value_store(self.kv_store_path))
        chain.add_peer(Peer())

        submitter = get_submitter()
        signing_identity = submitter.signing_identity
        # cc_instantiate_req = create_instantiation_proposal_req(
        #     CHAINCODE_NAME, CHAINCODE_PATH,
        #     CHAINCODE_VERSION, signing_identity,
        #     args=['a', '100', 'b', '200'])

        cc_instantiate_req = create_installment_proposal_req(
            CHAINCODE_NAME, CHAINCODE_PATH,
            CHAINCODE_VERSION, signing_identity,
        )

        queue = Queue(1)

        chain.instantiate_chaincode(cc_instantiate_req) \
            .subscribe(lambda x: queue.put(x))

        prop = queue.get(timeout=10)
        proposal_bytes = prop.proposal_bytes
        sig = prop.signature

        # verify the signature against the hash of proposal_bytes
        digest = signing_identity.msp.crypto_suite.hash(proposal_bytes)
        self.assertEqual(
            signing_identity.verify(str.encode(digest.hexdigest()),
                                    sig),
            True)
        self.shutdown_test_env()


if __name__ == '__main__':
    unittest.main()
