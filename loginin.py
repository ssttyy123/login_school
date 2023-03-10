import requests
from tkinter import messagebox


class Loginof(object):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.244.11&iTermType=1" \
          "&wlanuserip=10.161.164.49&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&ip=10" \
          ".161" \
          ".164.49&enAdvert=0&queryACIP=0&loginMethod=1"

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
              "Connection": "keep-alive",
              "Content-Length": "173",
              "Content-Type": "application/x-www-form-urlencoded",
              "Host": "10.10.244.11:801",
              "Origin": "http://10.10.244.11",
              "Referer": "http://10.10.244.11/",
              "Upgrade-Insecure-Requests": "1",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"}

    hasloginURL = "http://10.10.244.11:80/2.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255" \
                  ".252" \
                  ".150&mac=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=Mg%3D%3D"

    scURL = "http://10.10.244.11:80/3.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255.252.150" \
            "&mac=00-00-00-00-00-00&session="

    errmesURl_auten = "http://10.10.244.11/2.htm?wlanuserip=10.161.164.49&wlanacname=XL-BRAS-SR8806-X&wlanacip=10.255" \
                      ".252.150&mac=00-00-00-00-00-00&session=&ACLogOut=5&ErrorMsg=bGRhcCBhdXRoIGVycm9y"

    def __init__(self, schoolid, pas, operator):
        self.schoolid = schoolid
        self.pas = pas
        self.operator = operator

    def showof(self):
        print(self.schoolid, self.pas, self.operator)

    def on_login(self):
        self.data["DDDDD"] = ",0," + self.schoolid + "@" + self.operator
        self.data['upass'] = self.pas
        response = requests.post(self.url, self.data, self.header)
        rt = response.status_code
        print(response.url)
        if response.url == self.hasloginURL:
            return 1
        elif response.url == self.errmesURl_auten:
            messagebox.showwarning("用户验证失败，请检查用户名密码")
            return 2
        elif response.url == self.scURL:
            return 3
        # cmcc中国移动
        # chinanet中国联通
