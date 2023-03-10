import os
import json


class usersdata:
    def __init__(self):
        if not os.path.exists(r".\userdata.json"):
            self.fp = open(r".\userdata.json", 'w')
            basestruct = {'userdata': [
                {"id": "templateUser",
                 "pas": "123456",
                 "ope": 0}
            ],
                'default': {"id": "templateUser",
                            "pas": "123456",
                            "ope": 0,
                            'auto_start': 0}
            }
            # auto_start(0/1)不开机自启/开机自启
            json.dump(basestruct, self.fp, indent=4)
            self.fp.close()
            self.fp = open(r".\userdata.json")
            self.userlist = json.load(self.fp)
        else:
            self.fp = open(r".\userdata.json")
            self.userlist = json.load(self.fp)

    def writenewuser(self, userid, pas, ope):
        newuserdata = {"id": userid,
                       "pas": pas,
                       "ope": ope}
        self.fp.close()
        self.fp = open(r".\userdata.json", 'w')
        self.userlist['userdata'].append(newuserdata)
        json.dump(self.userlist, self.fp, indent=4)
        self.fp.close()
        self.fp = open(r".\userdata.json")
        self.userlist = json.load(self.fp)

    def readdata(self, userid):
        return self.userlist['userdata'][userid]

    def rutdefaultuesr(self):
        return self.userlist['default']

    def changefault(self, userid, pas, ope, auto_start):
        newuserdata = {"id": userid,
                       "pas": pas,
                       "ope": ope,
                       'auto_start': auto_start}
        self.fp.close()
        self.fp = open(r".\userdata.json", 'w')
        self.userlist['default'] = newuserdata
        json.dump(self.userlist, self.fp, indent=4)
        self.fp.close()
        self.fp = open(r".\userdata.json")
        self.userlist = json.load(self.fp)
