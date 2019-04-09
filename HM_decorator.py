import json
import hashlib
import logging
import os


class Country:
    def __init__(self, countries):
        self.countries = countries
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start != len(self.countries):
            return self.countries[self.start]['name']['common']
        else:
            raise StopIteration


with open("countries.json") as read_file:
    countries_info = json.load(read_file)
countries_name = Country(countries_info)

with open("country-link.txt", "w", encoding="utf8") as country_link:
    for country in countries_name:
        country_link.write(country + ' - ' + "https://en.wikipedia.org/wiki/" + country.replace(' ', '_') + '\n')


def logger_func(path):
    def logger_decor(old_function):
        logger = logging.getLogger('functions')
        logger.setLevel(logging.INFO)
        filename = os.path.join(path, 'functions.log')
        handler = logging.FileHandler(filename)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        def new_function(*args, **kwargs):
            logger.info('Start' + ' ' + old_function.__name__ +' with arguments: ' + str(args) + ' ' + str(kwargs))
            result = old_function(*args, **kwargs)
            logger.info('Finish with result' + ' ' + str(type(result)))
            return result
        return new_function
    return logger_decor

@logger_func('\\Netology')
def output_hash(file_name):
    hash_country = []
    with open(file_name) as read_file:
        for line in read_file:
            hash_country.append(hashlib.md5(line.encode()).digest())
    return hash_country


for line in output_hash("country-link.txt"):
    print(line)
