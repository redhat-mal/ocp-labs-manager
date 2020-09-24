from flask import Flask, Response
from manager_ocp4 import OCP4LabsManager
import os
import sys
import traceback
import json
import yaml

application = Flask(__name__)


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def getItemStatus(configData):
    returnConfig = []
    print("Labs Config:" + str(configData))

    for configItem in configData:
        print("ITEM:" + str(configItem))
        manager = ManagerFactory.getManager(configItem["name"], configItem["type"])
        configItem['status'] = manager.get_status()
        returnConfig.append(configItem);
    return returnConfig

@application.route("/lab-config")
def get_config():
    labsconfig = '{"labitems" : [] }'
    try:
       labsconfig = yaml.load(get_file("config/labs-config.yml"))
       labsconfig["labitems"] = getItemStatus(labsconfig["labitems"])
    except:
       print(traceback.format_exc())
       labsconfig = '{"labitems" : [] }'
    print("Labs Config:" + str(labsconfig))
    return labsconfig

@application.route("/install-item/<itemname>/<itemtype>")
def do_install(itemname, itemtype):
    print("Installing:" + itemname + " type:" + itemtype)
    status = '{"status" : "Installing" }'
    #try:
       #status = json.dumps(PodStatusReader().get_events(namespace,podname)) 
    #except:
    #   print(traceback.format_exc())
    #   status = '{"events" : "Pod Monitor Error"}'
    return status

@application.route("/css/lab-portal.css")
def page_style():
    content = get_file('css/lab-portal.css')
    return Response(content, mimetype="text/css")

@application.route("/")
def test_page():
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

class ManagerFactory:
    @staticmethod
    def getManager(itemname, itemtype):
        if itemtype == "ocp4":
            return OCP4LabsManager(itemname, itemtype)

if __name__ == "__main__":
    application.run(port=8080, host="0.0.0.0")
