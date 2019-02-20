import time
import requests
from pprint import pprint

class User:
    def __init__(self, friends, groups):
        self.friends = friends
        self.groups = groups
    # def get_uniq_groups(self, other):
    #     return self.groups

def get_friends_groups(method, user_id, token):
    params = {
        "access_token": token,
        "user_id": user_id,
        "v": "5.92"
    }
    api = "https://api.vk.com/method/" + method
    response = requests.get(api, params)
    getting_list = response.json()
    try:
        getting_list = set(getting_list["response"]["items"])
    except KeyError:
        getting_list = set()
    return getting_list

token = ""
user0 = 171691064

user_zero = User(get_friends_groups("friends.get", user0, token), get_friends_groups("groups.get", user0, token))
#pprint(user_zero.friends)

for other_user in user_zero.friends:
#    print(other_user)
    user_zero.groups = user_zero.groups.difference(get_friends_groups("groups.get", other_user, token))
    time.sleep(0.34)

pprint(user_zero.groups)
