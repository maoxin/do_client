from base import Base
import requests
import json

class Account(Base):
    """Account object to handler_log_in other thing"""
    def __init__(self, user_id=None, user_key=None, email=None):
        super(Account, self).__init__()
        self.user_id = user_id
        self.user_key = user_key
        self.email = email
        
        self.account_info = {
            'email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }
    
    def regist(self, user_name, email, phone_number, password):
        url = 'http://0.0.0.0:8888/register'
        
        account_info = {
            'user_name': user_name,
            'email': email,
            'phone_number': phone_number,
            'password': password,
        }
        
        info_json = json.dumps(account_info)
        
        message = {
            'JSON_REGISTER': info_json
        }
        
        response = requests.post(url, data=message)
        
        response_dic = json.loads(response.text)
        if response_dic['response'] != 'fail':
            self.user_id = response_dic['user_id']
            self.user_key = response_dic['user_key']
            self.email = email
            self.user_name = user_name
            
            self.account_info['email'] = self.email
            self.account_info['user_id'] = self.user_id
            self.account_info['user_key'] = self.user_key
        
            return response
            
        else:
            
            return 'fail'
            
    def log_in(self, log_in_tag, tag_info, password):
        url = 'http://0.0.0.0:8888/login'
        
        account_info = {
            'log_in_tag': log_in_tag,
            'tag_info': tag_info,
            'password': password,  
        }
        
        info_json = json.dumps(account_info)
        
        message = {
            "JSON_LOGIN": info_json,
        }
        
        response = requests.post(url, data=message)
        
        response_dic = json.loads(response.text)
        if response_dic['response'] != 'fail':
            self.user_id = response_dic['user_id']
            self.user_key = response_dic['user_key']
            
            self.email = response_dic['email']
            self.user_name = response_dic['user_name']
            
            self.account_info['email'] = self.email
            self.account_info['user_id'] = self.user_id
            self.account_info['user_key'] = self.user_key
        
            return response
            
        else:
            
            return 'fail'
            
    def look_my_profile(self):
        url = 'http://0.0.0.0:8888/look_my_profile'
        
        info_json = json.dumps(self.account_info)
        
        message = {
            'JSON_LOOK_OWN_PROFILE': info_json
        }
        
        response = requests.post(url, data=message)
        response_dic = json.loads(response.text)
        
        return response_dic
        
        
        
        
           
def get_register():    
    account = Account()
    
    response = account.regist('maoxin', 'maoxin.horizon@gmail.com', 18810496259, 'Myahoo445')
    
    return account, response
    
def get_log_in():
    account = Account()
    
    response = account.log_in('email', 'maoxin.horizon@gmail.com', 'Myahoo445')
    
    return account, response
