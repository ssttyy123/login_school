import time

import requests
import re
import os
from tkinter import messagebox


class Loginof(object):
    wifiurl = "http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn" \
              "&iTermType=1&wlanuserip=10.163.177.171&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00" \
              "-00-00-00-00&ip=10.163.177.171&enAdvert=0&queryACIP=0&loginMethod=1"

    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.244.11&iTermType=1" \
          "&wlanuserip=10.161.164.49&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&ip=10" \
          ".161.164.49&enAdvert=0&queryACIP=0&loginMethod=1"

    data = {"DDDDD": "",
            "upass": "",
            "R1": "0",
            "R2": "0",
            "R3": "0",
            "R6": "0",
            "para": "00",
            "0MKKey": "123456"}

    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                        "application/signed-exchange;v=b3;q=0.7",
              "Accept-Encoding": "gzip, deflate",
              "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
              "Cache-Control": "max-age=0",
              "Connection": "close",
              "Content-Length": "173",
              "Content-Type": "application/x-www-form-urlencoded",
              "Host": "10.10.244.11:801",
              "Origin": "http://10.10.244.11",
              "Referer": "http://10.10.244.11/",
              "Upgrade-Insecure-Requests": "1",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"}

    warningmess = {
        "http://10.10.244.11:80/2.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150"
        "&mac=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=Mg%3D%3D": 1,

        "http://10.10.244.11:80/3.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150"
        "&mac=00-00-00-00-00-00&session=": 0,

        "http://p.njupt.edu.cn/3.htm?wlanuserip=10.163.135.80&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X"
        "&account=B21120202@cmcc": 0,

        "http://p.njupt.edu.cn:80/3.htm?wlanuserip=10.163.177.171&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150"
        "&mac=00-00-00-00-00-00&session=": 0,

        "http://10.10.244.11/2.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150&mac"
        "=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=bGRhcCBhdXRoIGVycm9y": 2,

        "http://p.njupt.edu.cn/2.htm?wlanuserip=10.163.135.80&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150&mac"
        "=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=NTEy": 3,

        "http://p.njupt.edu.cn/2.htm?wlanuserip=10.163.135.80&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150&mac"
        "=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=dXNlcmlkIGVycm9yMQ%3D%3D": 4
    }
    '''
    0.You have successfully logged into our system.
    1.IP already online
    2.Failed to authenticate user
    3.Please check the network configuration and confirm the account number and password is correct！ 
    4.Account does not exist or not bind isp account.
    20.unknowerr
    '''

    opelist = {'中国移动': 'cmcc',
               '中国联通': 'njxy'}

    def __init__(self, schoolid, pas, operator):
        self.schoolid = schoolid
        self.pas = pas
        self.operator = operator

    def showof(self):
        print(self.schoolid, self.pas, self.opelist[self.operator])

    def on_login(self):
        self.data["DDDDD"] = ",0," + self.schoolid + "@" + self.opelist[self.operator]
        self.data['upass'] = self.pas
        proxies = {'http': None,
                   'https': None}
        # Wi-Fi mywlan 1/officwlan 2
        flag = 0
        result = os.popen('netsh WLAN show interfaces')
        context = result.read()
        if re.search("SSID                   :", context) is None:
            while 1:
                time.sleep(2)
                result = os.popen('netsh WLAN show interfaces')
                context = result.read()
                if re.search("SSID                   :", context) is not None:
                    break

        wlan_type = context[re.search("SSID                   :", context).span()[1] + 1:
                            re.search("BSSID", context).span()[0] - 5]
        if wlan_type == "NJUPT-CMCC" or wlan_type == "NJUPT-CHINANET":
            self.header["Host"] = "p.njupt.edu.cn:801"
            self.header["Origin"] = "http://p.njupt.edu.cn"
            self.header["Referer"] = "http://p.njupt.edu.cn/"
            self.header["Connection"] = "close"
            flag = 2
        else:
            self.header["Host"] = "10.10.244.11:801"
            self.header["Origin"] = "http://10.10.244.11"
            self.header["Referer"] = "http://10.10.244.11/"
            self.header["Connection"] = "keep-alive"
            flag = 1

        response = requests.post(self.url if flag == 1 else self.wifiurl, self.data, self.header, proxies=proxies)
        rt = response.status_code
        print(response.url)
        if response.url in self.warningmess:
            return self.warningmess[response.url]
        else:
            print(self.url if flag == 1 else self.wifiurl)
            print(wlan_type)
            print(self.data)
            print(self.header)
            return 20
