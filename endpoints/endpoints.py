import sys
sys.path.append("../")
from libraries.libraries import *

class endpoints():
    def __init__(self):
        pass
    def links(space_id, folder_id):
        endpoints = {
            "teams": "https://api.clickup.com/api/v2/team",
            "space": "https://api.clickup.com/api/v2/space/" + space_id,
            "folder": "https://api.clickup.com/api/v2/space/" + folder_id
            "lists": "https://api.clickup.com/api/v2/folder/" + folder_id + "/list",
            "tasks": "",
        }
        
        return endpoints