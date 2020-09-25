from manager_base import AbstractLabsManager
import logging
import labsmgr
import subprocess

class HelmLabsManager(AbstractLabsManager):

    def __init__(self, itemName, config_dir, item_vars, status='new'):
        super().__init__(itemName, config_dir, item_vars)
        logging.info("Helm Logging manager for: %s", itemName)

    def get_status(self):
        status = "new"
        try:
            logging.info("Getting helm status for %s, namespace: %s", self.lab_name, self.item_vars);
            #status = super().get_file("install-status.sh")
            #procStatus = subprocess.run( [super().root_dir() + 'status.sh', self.lab_name], capture_output=True)
            process = subprocess.Popen([super().root_dir() + 'status.sh', self.item_vars['namespace']['value']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            logging.info("Process complete: %s", str(out))
            status = str(out, "utf-8")
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
            subprocess.call( [super().root_dir() + 'install.sh' , self.item_vars['namespace']['value']]) 
        except Exception as err:
            logging.error("Error: %s", str(err))
            status = {"status" : "error", "message" : str(err) }
        return status

    def do_remove(self, itemname):
       logging.info("Starting remove for: %s", itemname)
       status = {"status" : "ok"}
       try:
          subprocess.call( [super().root_dir() + 'destroy.sh' , self.item_vars['namespace']['value']])
       except Exception as err:
           logging.error("Error: %s", str(err))
           status = {"status" : "error", "message" : str(err) }
       return status

