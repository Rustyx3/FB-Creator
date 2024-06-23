import requests
import random
import string
import json
import hashlib, threading 
import gzip
from faker import Faker

# Setup Chrome options and user agent for Selenium WebDriver
USERNAME = "IP-USERNAME"
PASSWORD = "PASS"
ENDPOINT = "PORT"

def get_chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    return {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"http://{user}:{password}@{endpoint}",
        },
        "verify_ssl": False,
    }

proxy_options = get_chrome_proxy(USERNAME, PASSWORD, ENDPOINT)

def follow(token):
 yourid='profile-id'
 followid='follow-id'
 type='PROFILE'#PROFILE/PAGE
 headers = {"Authorization": f"OAuth {token}","X-FB-Connection-Type": "WIFI","X-FB-HTTP-Engine": "Apache","Content-Type": "application/json","Host": "graph.facebook.com","Connection": "Keep-Alive","User-Agent": "FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/447626277;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBCR/;FBMF/SPA Condor Electronics;FBBD/Condor;FBPN/com.facebook.katana;FBDV/Plume L2;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;","Accept-Encoding": "gzip"}
 data = {"query_id": "page-id","method": "post","strip_nulls": "true","query_params": {"input": {"actor_id":yourid,"client_mutation_id": "78e8e21c-7b3b-4f93-a806-1f84158b8c54","subscribe_location": "PROFILE","subscribee_id": followid}},"locale": "en_US","client_country_code": "US","fb_api_req_friendly_name": "ActorSubscribeCoreMutation","fb_api_caller_class": "com.facebook.friends.protocol.FriendMutationsModels$ActorSubscribeCoreMutationFieldsModel"}
 encoded_data = gzip.compress(json.dumps(data).encode('utf-8'))
 response = requests.post('https://graph.facebook.com/graphql', data=encoded_data, headers=headers)
 print('[+] Follow Response : '+'{"actor_subscribe":{"subscribee":{"__type__":{"name":"User"},"id":"profile-id","subscribe_status":"IS_SUBSCRIBED"}}}')
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def create_mail_tm_account():
    fake = Faker()
    mail_domains = 'yopmail.com'
    if mail_domains:
        domain = mail_domains
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        return f"{username}@{domain}", password, first_name, last_name, birthday
def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,'attempt_login': False,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': False}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    print(f'''[+] Email : {email}
[+] ID : {id}
[+] Token : {token}
[+] PassWord : {password}
[+] Name : {first_name} {last_name}
[+] BirthDay : {birthday}
[+] Gender : {gender}
===================================''')
#    follow(token)
def _call(url, params, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

while True:
 email, password, first_name, last_name, birthday = create_mail_tm_account()
 if email and password and first_name and last_name and birthday:
  register_facebook_account(email, password, first_name, last_name, birthday)