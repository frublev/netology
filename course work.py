import time
import requests
import json
# from pprint import pprint


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


def separate_groups(user0, token):
    user_zero = User(get_friends_groups("friends.get", user0, token), get_friends_groups("groups.get", user0, token))
    print("Список групп и друзей пользователя получен")
    user_count = len(user_zero.friends)
    i = 0
    for other_user in user_zero.friends:
        user_zero.groups = user_zero.groups.difference(get_friends_groups("groups.get", other_user, token))
        time.sleep(0.34)
        i += 1
        print("\rПоиск уникальных групп. Выполнено", round(i / user_count * 100), "%", end="")
    return ",".join(map(str,list(user_zero.groups)))


def get_groups_info(groups):
    params = {
        "access_token": token,
        "group_ids": groups,
        "fields": "name,id,members_count",
        "v": "5.92"
    }
    api = "https://api.vk.com/method/groups.getById"
    response = requests.get(api, params)
    getting_info = response.json()
    groups_info = []
    for group in getting_info["response"]:
        groups_info.append({"name": group["name"], "gid": group["id"], "members_count": group["members_count"]})
    return groups_info

def write_file(file_name, user0, token):
    with open(file_name, "w") as uniq_groups:
        data = get_groups_info(separate_groups(user0, token))
        json.dump(data, uniq_groups, sort_keys = True, indent = 4, ensure_ascii = False)
        print("\nФайл записан")


if __name__ == "__main__":
    file_name = "uniq_groups.json"
    token = ""
    user0 = 171691064
    write_file(file_name, user0, token)
