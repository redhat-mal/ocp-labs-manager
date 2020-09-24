from manager_base import AbstractLabsManager
import logging
import labsmgr
import subprocess

class OCP4LabsManager(AbstractLabsManager):

    def __init__(self, itemName, status='new'):
        super().__init__(itemName)
        logging.info("OCP4 Logging manager for: %s", itemName)

    def get_status(self):
        status = "new"
        try:
            logging.info("Getting ocp4 cluster status");
            status = super().get_file("install-status")
            if status:
                status = status.strip('\n')
        except Exception as err:
            logging.warn("Getting Status file:" + str(err));
            pass
        return status

    def do_install(self, itemname):
        logging.info("Starting install for: %s", itemname)
        status = {"status" : "ok"}
        try:
            subprocess.call( [super().root_dir() + 'install.sh' , super().root_dir()]) 
        except Exception as err:
            logging.error("Error: %s", str(err))
            status = {"status" : "error", "message" : str(err) }
        return status

    def do_remove(self, itemname):
       logging.info("Starting remove for: %s", itemname)
       status = {"status" : "ok"}
       try:
          subprocess.call( [super().root_dir() + 'destroy.sh' , super().root_dir()])
       except Exception as err:
           logging.error("Error: %s", str(err))
           status = {"status" : "error", "message" : str(err) }
       return status

