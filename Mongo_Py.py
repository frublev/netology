import csv
import re
import pymongo
from pymongo import MongoClient

client = MongoClient()
artist_db = client['artist']
tickets = artist_db['tickets']

def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    data = []
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.reader(csvfile)
        next(reader)
        for line in reader:
            artist, price, place, date = line
            price = int(price)
            data.append({
                'artist': artist,
                'price': price,
                'place': place,
                'date': date
            })
    db.insert_many(data)


def find_cheapest(db, count):
    """
    Найти самые дешевые билеты
    Документация: https://docs.mongodb.com/manual/reference/operator/aggregation/sort/
    """
    return db.find().sort([('price', 1)]).limit(count)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и выведите их по возрастанию цены
    """
    regex = re.compile(re.escape(name), re.IGNORECASE)
    return db.find({'artist': regex}).sort([('price', pymongo.ASCENDING)])


if __name__ == '__main__':
    read_data('artist.csv', tickets)
    a = find_cheapest(artist_db.tickets, 3)
    print(list(a))
    b = find_by_name('.', artist_db.tickets)
    print(list(b))
