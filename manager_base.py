from abc import abstractmethod
import os
import logging
import labsmgr

class AbstractLabsManager:

    def __init__(self, lab_name, config_dir, item_vars):
        """Constructor"""
        self.lab_name = lab_name
        self.config_dir = config_dir
        self.item_vars = item_vars

    @abstractmethod
    def get_status(self):
        # This will be tracker specific
        pass

    @abstractmethod
    def do_install(self, itemname):
        # This will be tracker specific
        pass

    @abstractmethod
    def do_remove(self, itemname):
        # This will be tracker specific
        pass

    def root_dir(self):  # pragma: no cover
      return os.path.abspath(os.path.dirname(__file__)) + "/config/" + self.config_dir + "/"

    def get_file(self, filename):  # pragma: no cover
        logging.info("Reading File: %s, , %s", self.root_dir(), filename)

        src = os.path.join(self.root_dir() + filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()

