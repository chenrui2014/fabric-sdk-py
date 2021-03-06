# Copyright arxanfintech.com 2016 All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

from hfc.fabric.chain.chain import Chain


class Client(object):
    """
        Main interaction handler with end user.
        Client can maintain several chains.
    """

    def __init__(self):
        self.chains = {}
        self.state_store = None
        self.crypto_suite = None
        self.user_context = None
        self.logger = logging.getLogger(__name__)
        self.logger.info('Init Client')

    def new_chain(self, name):
        """Init a chain instance with given name.

        :param name: The name of chain

        :return: The inited chain instance
        """
        self.logger.debug("New a chain with name = {}".format(name))
        if name not in self.chains:
            self.chains[name] = Chain(name)
        return self.chains[name]

    def get_chain(self, name):
        """ Get a chain instance

        :param name: the name of the chain

        :return: Get the chain instance with the name or None
        """
        return self.chains.get(name, None)

    def set_crypto_suite(self, crypto_suite):
        """Set the crypto suite to given one.

        Args:
            crypto_suite: The crypto_suite to use.

        Returns: None

        """
        self.crypto_suite = crypto_suite

    def get_crypto_suite(self):
        """Get the crypto suite.

        Returns: The crypto_suite instance or None

        """
        return self.crypto_suite

    def set_state_store(self, store):
        """store user enrollment materials. The SDK should make this
        pluggable so that different store implementations can be
        selected by the application. For instance, in some cases
        File-based stores a sufficient. But for clustering purposes,
        multiple application instances want to share a store backed
        by a database.

        :param store: instance of an alternative KeyValueStore
        implementation provided by the consuming app

        :return: None
        """
        self.state_store = store

    def set_logger(self, logger):
        """Sets an instance of a logger used by the consuming application.
        This is useful because an application would likely want to use a
        common logger for all parts of the code.
        And typically an IT organization would have log scraping set up for
        monitoring and analytics purposes, such that a 'standard' log format
        is desirable.
        The SDK should have a built-in logger so that developers get logging by
        default.
        But it MUST allow an external logger to be set with a standard set of
        logging APIs

        :param logger: an external logging utility that implements a standard
        interface.

        :return: None
        """
        self.logger = logger

    def new_state_store(self, **options):
        """Create a state store with given parameters
        store or change persistent and private data
        Params

        :param name:The name of the key
        :return: the result

        """
        pass
