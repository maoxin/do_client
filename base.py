class Base(object):
    """Base for every class for the user_id, user_key"""
    def __init__(self):
        self.user_id = None
        self.user_key = None
        self.user_name = None
        self.email = None
        
        self.account_info = {
            'email': self.email,
            'user_id': self.user_id,
            'user_key': self.user_key,
        }