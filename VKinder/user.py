import vk_api

class User:
    def __init__(self, id, sex, place, age, friends=[], groups=[], interests=[], music=[], books=[]):
        self.id = id
        self.sex = sex
        self.place = place
        self.age = age
        self.friends = friends
        self.groups = groups
        self.interests = interests
        self.music = music
        self.books = books

    def creat_request(self):
        if self.sex == 1:
            sex = 2
        else:
            sex = 1
        if self.age < 18:
            raise Exception('You are too young!')
        if self.sex == 1:
            age_from = self.age - 2
            age_to = self.age + 6
        else:
            age_from = self.age - 6
            age_to = self.age + 2
        if age_from < 18:
            age_from = 18
        age_range = age_to - age_from

        params = {
            'sort': 0,
            'count': 1000,
            'sex': sex,
            'age_from': age_from,
            'age_to': age_from,
            'birth_month': 1,
            'city': self.place,
            'has_photo': 1,
            'fields': '',
            'offset': 0,
            'status': 7,
            'fields': 'interests,music,books'
        }
        return Request_vk(params, age_range)

class Request_vk:
    def __init__(self, params, age_range):
        self.params = params
        self.age_range = age_range

    def get_candidate(self, vk, db):
        with vk_api.VkRequestsPool(vk) as pool:
            for r in range(self.age_range):
                for m in range(12):
                    user_list = []
                    user = vk.users.search(**self.params)
                    for i in user['items']:
                        user_info = {'id': i['id'], 'age': self.params['age_from'], 'interests': i.get('interests'),
                                      'music': i.get('music'), 'books': i.get('books')}
                        user_list.append(user_info)
                    db.insert_many(user_list)
                    self.params['birth_month'] += 1
                self.params['age_from'] = self.params['age_from'] + 1
                self.params['age_to'] = self.params['age_to'] + 1
                self.params['birth_month'] = 1
