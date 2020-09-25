from flask import Flask, Response
from manager_ocp4 import OCP4LabsManager
from manager_helm import HelmLabsManager
import os
import sys
import traceback
import json
import yaml
import logging
import labsmgr

application = Flask(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def getItemConfig(itemname):
    logging.info("Getting  Config for: %s", itemname)
    configData = yaml.load(get_file("config/labs-config.yml"))
    for configItem in configData["labitems"]:
        if configItem["name"] == itemname:
            return configItem
    return []


def getItemStatus(configData):
    returnConfig = []
    logging.info("Labs Config:" + str(configData))

    for configItem in configData:
        logging.info("Get Items, name: %s, type: %s, config_dir: %s, vars: %s", 
                configItem["name"], configItem["type"], configItem["config-dir"], configItem['vars'])
        manager = ManagerFactory.getManager(configItem["name"], configItem["type"], configItem["config-dir"], configItem["vars"])
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
       logging.error(traceback.format_exc())
       labsconfig = '{"labitems" : [] }'
    logging.info("Labs Config:" + str(labsconfig))
    return labsconfig

@application.route("/install-item/<itemname>/<itemtype>")
def do_install(itemname, itemtype):
    logging.info("Installing:" + itemname + " type:" + itemtype)
    status = {"status" : "None" }
    try:
        itemConfig = getItemConfig(itemname)
        logging.info("Installing name: %s, type: %s, configData: %s", itemname, itemtype, str(itemConfig))
        manager = ManagerFactory.getManager(itemname, itemtype, itemConfig['config-dir'], itemConfig['vars'])
        status = manager.do_install(itemname)
    except Exception as ex:
       logging.error("Error on install: %s", str(ex))
       status = {"status" : "failed" , "message" : str(ex) }
    return status

@application.route("/remove-item/<itemname>/<itemtype>")
def do_remove(itemname, itemtype):
    logging.info("Removing:" + itemname + " type:" + itemtype)
    status = {"status" : "None" }
    itemConfig = getItemConfig(itemname)
    try:
        manager = ManagerFactory.getManager(itemname, itemtype, itemConfig['config-dir'], itemConfig['vars'])
        status = manager.do_remove(itemname)
    except Exception as ex:
       logging.error("Error on install: %s", str(ex))
       status = {"status" : "failed" , "message" : str(ex) }
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
    def getManager(itemname, itemtype, config_dir, item_vars):
        if itemtype == "ocp4":
            return OCP4LabsManager(itemname, config_dir, item_vars)
        if itemtype == "helm":
            return HelmLabsManager(itemname, config_dir, item_vars)

if __name__ == "__main__":
    application.run(port=8080, host="0.0.0.0")
