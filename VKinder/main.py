import vk_api
import requests
import json
import datetime
from datetime import datetime
from VKinder.user import User, Request_vk
import pymongo
from pymongo import MongoClient

client = MongoClient()
vk_users_db = client['vk_users']
vkinder = vk_users_db['vkinder']

API_VERSION = '5.92'
APP_ID = 6972761
TOKEN = ''
connect_params = {'token': TOKEN, 'app_id': APP_ID, 'api_version': API_VERSION}

def vk_connect(connect_params):
    vk_session = vk_api.VkApi(**connect_params)
    vk = vk_session.get_api()
    return vk

def get_user(vk, user_id):
    params = {
        "user_ids": user_id,
        "fields": "sex,bdate,city,interests,music,books",
        "v": "5.92"
    }
    with vk_api.VkRequestsPool(vk) as pool:
        user = vk.users.get(**params)
        friends = vk.friends.get(user_id=user_id)
        groups = vk.groups.get(user_id=user_id)
    age = get_age(user[0]['bdate'])
    friends = friends['items']
    groups = groups['items']
    interest = user[0]['interests'].split(',')
    music = user[0]['music'].split(',')
    books = user[0]['books'].split(',')
    user0 = User(
        user[0]['id'],
        user[0]['sex'],
        user[0]['city']['id'],
        age,
        friends, groups,
        interest, music, books)
    return user0

def get_age(str):
    age = datetime.now() - datetime.strptime(str, '%d.%m.%Y')
    age = int(age.days/365)
    return age

vk = vk_connect(connect_params)
user = get_user(vk, 532061280)
request = user.creat_request()
request.get_candidate(vk, vkinder)
