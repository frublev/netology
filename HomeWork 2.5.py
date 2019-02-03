from datetime import datetime
class CodeTimer:
  def __init__(self, start = datetime.now()):
    self.start = datetime.now()
  def __enter__(self):
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.end = datetime.now()
    print("Время запуска кода:", self.start)
    print("Время остановки кода:", self.end)
    print("Время исполнения кода:", self.end - self.start)

def cookbook_load(cookbook_name):
  cook_dict = {}
  with open(cookbook_name, mode="r", encoding="utf-8") as f_cook_book:
      for line in f_cook_book:
        dishes = line.strip()
        cook_dict[dishes] = list()
        ingr_num = int(f_cook_book.readline())
        for i in range (0, ingr_num):
          ingedients_dict = {}
          ingredient = f_cook_book.readline().split(" | ")
          ingedients_dict['ingridient_name'] = ingredient[0]
          ingedients_dict['quantity'] = int(ingredient[1])
          ingedients_dict['measure'] = ingredient[2].strip()
          cook_dict[dishes].append(ingedients_dict)
        f_cook_book.readline()
  return cook_dict

def get_shop_list_by_dishes(dishes, person_count):
   cook_dict = cookbook_load(r"C:\Users\admin\PycharmProjects\netology\venv\cookbook.txt")
   shop_list = {}
   for dish in dishes:
     for ingredient in cook_dict[dish]:
       if ingredient["ingridient_name"] in shop_list.keys():
         shop_list[ingredient["ingridient_name"]]["quantity"] += ingredient["quantity"] * person_count
       else:
         shop_list[ingredient["ingridient_name"]] = {'measure': ingredient['measure'], 'quantity' : ingredient['quantity'] * person_count}
   print(shop_list)

if __name__ == '__main__':
   with CodeTimer() : get_shop_list_by_dishes(["Омлет", "Фахитос"], 10)