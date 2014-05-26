from base import Base
from datetime import datetime
import requests
import json

class Item(object):
    """Item Object To Handle item post and others"""
    def __init__(self, account):
        super(Item, self).__init__()
        self.user_id = account.user_id
        self.user_key = account.user_key
        self.user_name = account.user_name
        self.email = account.email
        
        self.account_info = {
            'email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }
        
    def post_item(self, mission_info):
        url = 'http://0.0.0.0:8888/item/post_item'
        
        mission_info['mission_up_email'] = self.email
        mission_info['user_id'] = self.user_id
        mission_info['user_key'] = self.user_key
        mission_info['mission_up_name'] = self.user_name
        
        info_json = json.dumps(mission_info)
        message = {
            'JSON_CREATE_ITEM': info_json
        }
        
        response = requests.post(url, data=message)
        
        return response
    
    def get_new_items(self, ids=[]):
        url = 'http://0.0.0.0:8888/item/get_new_item'
        
        ids_info = {
            'ids': ids,
        }
        
        info_json = json.dumps(ids_info)
        message = {
            'JSON_GET_NEW_ITEM': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
        
    def get_item_in_map(self, ids=[]):
        url = 'http://0.0.0.0:8888/item/get_item_in_map'
        
        ids_info = {
            'ids': ids,
        }
        
        info_json = json.dumps(ids_info)
        message = {
            'JSON_ITEM_IN_MAP': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
        
    def recieve_item(self, mission_id):
        url = 'http://0.0.0.0:8888/item/receive'
        
        ask_info = {
            'mission_id': mission_id,
            'join_email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }
        
        info_json = json.dumps(ask_info)
        
        message = {
            'JSON_RECEIVE_ITEM': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
        
    def delete_item(self, mission_id):
        url = 'http://0.0.0.0:8888/item/delete'
        
        ask_info = {
            'mission_id': mission_id,
            
            'mission_up_email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }
        
        info_json = json.dumps(ask_info)
        message = {
            'JSON_DELETE_ITEM': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
        
    def archive_item(self, mission_id):
        url = 'http://0.0.0.0:8888/item/archive'
        
        ask_info = {
            'mission_id': mission_id,
            
            'mission_up_email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }
        
        info_json = json.dumps(ask_info)
        message = {
            'JSON_ARCHIVE_ITEM': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
    
    def item_detail(self, mission_id):
        url = 'http://0.0.0.0:8888/item/detail'
        
        ask_info = {
            'mission_id': mission_id,
        }
        
        info_json = json.dumps(ask_info)
        message = {
            'JSON_GET_MISSION_MORE': info_json,
        }
        
        response = requests.post(url, data=message)
        
        return response
        
    
        

def create_mission_info():
    mission_info = {
        'mission_tag': ['mao', 'xin', 'kingdom'],
        'mission_name': 'reinforce the kingdom',
        'mission_description': 'protect the kingdom from the bad man',
        
        'mission_place_name': 'bad place',
        'mission_lat': 2048,
        'mission_lon': 1024,
        
        'user_place_name': 'good place',
        'user_lat': 1024,
        'user_lon': 2048,
        
        'mission_begin_time': str(datetime.now()),
        'mission_continue': 12,
        
        'mission_accept_num': 5,
    }
    
    return mission_info
    
        
        
        

      
        
