import os
import json


class usersdata:
    def __init__(self):
        if not os.path.exists(".\\userdata.json"):
            self.fp = open(".\\userdata.json", 'w')
            basestruct = {'userdata': [
                {"id": "templateUser",
                 "pas": "123456",
                 "ope": 0}
            ],
                'default': {"id": "templateUser",
                            "pas": "123456",
                            "ope": 0}
            }
            json.dump(basestruct, self.fp, indent=4)
            self.fp.close()
            self.fp = open(".\\userdata.json")
            self.userlist = json.load(self.fp)
        else:
            self.fp = open(".\\userdata.json")
            self.userlist = json.load(self.fp)

    def writenewuser(self, userid, pas, ope):
        newuserdata = {"id": userid,
                       "pas": pas,
                       "ope": ope}
        self.fp.close()
        self.fp = open(".\\userdata.json", 'w')
        self.userlist['userdata'].append(newuserdata)
        json.dump(self.userlist, self.fp, indent=4)
        self.fp.close()
        self.fp = open(".\\userdata.json")
        self.userlist = json.load(self.fp)

    def readdata(self, userid):
        return self.userlist['userdata'][userid]

    def rutdefaultuesr(self):
        return self.userlist['default']
