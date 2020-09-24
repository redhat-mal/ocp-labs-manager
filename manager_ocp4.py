from manager_base import AbstractLabsManager
import logging
import labsmgr

class OCP4LabsManager(AbstractLabsManager):

   def __init__(self, itemName, status='new'):
       super().__init__(itemName)
       logging.info("OCP4 Logging manager for: %s", itemName)

   def get_status(self):
      status = "new"
      try:
        logging.info("Getting ocp4 cluster status");
        status = super().get_file("install-status")
      except Exception as err:
          print("ERROR Getting Status:" + str(err));
          pass
      return status
