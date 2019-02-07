import json
import xml.etree.ElementTree as ET


def analyse_json_file(json_file):
    with open(json_file, mode="r", encoding="utf-8") as news_file:
        afr_news = json.load(news_file)
        news_items = afr_news["rss"]["channel"]["items"]
    descriptions = ""
    for item in news_items:
        descriptions += " " + item["description"]
    return descriptions


def analyse_xml_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    news_items = root.findall("channel/item/description")
    descriptions = ""
    for items in news_items:
        descriptions += items.text
    return descriptions


def word_count(descriptions):
    descriptions = descriptions.lower()
    word_list = descriptions.strip().split()
    i = 0
    while i < len(word_list):
        if len(word_list[i]) < 7:
            del word_list[i]
        else:
            i += 1
    words = {}
    for word in word_list:
        if word not in words:
            words[word] = word_list.count(word)
    words = list(words.items())
    words.sort(key=lambda word: word[1], reverse=True)
    return words


description = analyse_xml_file("newsafr.xml")

word_in_news = word_count(description)

for i in range(10):
  print(word_in_news[i])
