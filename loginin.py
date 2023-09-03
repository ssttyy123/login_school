import json
import re

import requests


class Loginof(object):
    wlanip = ""

    urlM = "https://p.njupt.edu.cn:802/eportal/portal/login/"

    params = {
        "callback": "dr1003",
        "login_method": "1",
        "user_account": "",
        "user_password": "",
        "wlan_user_ip": "10.161.164.49",
        "wlan_user_ipv6": "",
        "wlan_user_mac": "000000000000",
        "wlan_ac_ip": "",
        "wlan_ac_name": "",
        "jsVersion": "4.1.3",
        "terminal_type": "1",
        "lang": "zh-cn",
        "v": "5614"
    }

    header = {
        "authority": "p.njupt.edu.cn:802",
        "method": "GET",
        "path": "",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Referer": "https://p.njupt.edu.cn/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Microsoft Edge\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"}

    opelist = {'中国移动': 'cmcc',
               '中国联通': 'njxy'}

    def __init__(self, schoolid, pas, operator):
        self.params["user_account"] = ",0," + schoolid + "@" + self.opelist[operator]
        self.params["user_password"] = pas

    def on_login(self):
        # proxies = {'http': None,
        #            'https': None}
        rt = ()
        try:
            response = requests.get(url=self.urlM, params=self.params, headers=self.header)
            json_str = re.findall(r"dr1003\((.+?)\);", response.text)
            print(json_str[0])
            json_ob = json.loads(json_str[0])
            if int(json_ob["result"]) == 0:
                rt = (0, json_ob["ret_code"])
            elif int(json_ob["result"]) == 1:
                rt = (1, 0)
            return rt
        except requests.exceptions.SSLError:
            print("no network")
            rt = (3, 0)
        return rt
