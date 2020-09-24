from abc import abstractmethod
import os
import logging
import labsmgr

class AbstractLabsManager:

    def __init__(self, lab_name):
        """Constructor"""
        self.lab_name = lab_name

    @abstractmethod
    def get_status(self):
        # This will be tracker specific
        pass

    def root_dir(self):  # pragma: no cover
      return os.path.abspath(os.path.dirname(__file__)) + "/config/" + self.lab_name + "/"

    def get_file(self, filename):  # pragma: no cover
      try:
        logging.info("Reading File: %s, , %s", self.root_dir(), filename)

        src = os.path.join(self.root_dir() + filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
      except IOError as exc:
        logging.error("Error:" + exc)
        return str(exc)

