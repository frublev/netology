documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006"}
]

#"name": "Аристарх Павлов"

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def find_name():
  document_num = input("Введите номер документа:")
  for document in documents:
    if document["number"] == document_num:
      holder_name = document["name"]
      break
    else:
      holder_name = "Документ отсутствует"
  print("Владелец:", holder_name)
  return holder_name

def print_list():
  for case in documents:
    print(case["type"], ' "', case["number"], '" "', case["name"], '"', sep="")
#print_list()

def find_shelf():
  document_num = input("Введите номер документа:")
  for shelf_num in directories:
    if document_num in directories[shelf_num]: break
    else:
      shelf_num = "Документ отсутствует на полках"
  return shelf_num
#print(find_shelf())

def add_doc():
  document_type = input("Введите тип документа:")
  document_num = input("Введите номер документа:")
  holder_name = input("Введите имя владельца:")
  shelf_num = input("Введите номер полки для хранения:")
  documents.append({"type": document_type, "number": document_num, "name": holder_name})
  if shelf_num in directories.keys():
    directories[shelf_num].append(document_num)
  else:
    directories[shelf_num] = [document_num]

def show_name():
  for person in documents : print(person["name"])

command = input("Введите команду:")
if command == "p":
  find_name()
elif command == "l":
  print_list()
elif command == "s":
  print(find_shelf())
elif command == "a":
  add_doc()
  print(documents, directories)
elif command == "n":
  try:
    show_name()
  except KeyError:
    print("Отсутствует ключ в словаре")