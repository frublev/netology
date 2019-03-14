class Contact:
    def __init__(self, name, sur_name, phone, favourite_contact=False, *args, **kwargs):
        self.name = name
        self.surname = sur_name
        self.phone = phone
        self.favourite_contact = favourite_contact
        self.kwargs = kwargs

    def __str__(self):
        if self.favourite_contact:
            self.favourite_contact = "да"
        else:
            self.favourite_contact = "нет"
        output = "Имя: " + self.name + "\n" + "Фамилия: " + self.surname + "\n" + "Телефон: " + self.phone + "\n" + "В избранных: " + self.favourite_contact + "\n"
        output += "Дополнительная информация:" + "\n"
        for contact_type, contact_address in self.kwargs.items():
            output += ("         " + contact_type + " : " +contact_address + "\n")

        return output


class PhoneBook:
    def __init__(self, name_book, contacts=[]):
        self.name_book = name_book
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def print_book(self):
        for contact in self.contacts:
            print(str(contact))

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone == phone_number:
                self.contacts.remove(contact)

    def find_favourite(self):
        for contact in self.contacts:
            if contact.favourite_contact:
                print(str(contact))

    def find_contact(self, name_surname):
        for contact in self.contacts:
            if contact.name + " " + contact.surname == name_surname:
                print(str(contact))


if __name__ == "__main__":
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    mary = Contact('Mary', 'Lee', '+7987654321', favourite_contact=True, telegram='@mary', email='mary@lee.com')
    richard = Contact('Richard', 'Doe', '+710101010', favourite_contact=True, telegram='@richard', email='richard@doe.com')
    ronald = Contact('Ronald', 'MacDonald', '+720202020', telegram='@ronald', email='ronald@macdonald.com')
    lisa = Contact('Lisa', 'Simpson', '+730303030', favourite_contact=True, telegram='@lisa', email='lisa@simpson.com')
    contacts = [jhon, mary, richard, ronald, lisa]
    my_phone_book = PhoneBook("Моя телефонная книга")

    for contact in contacts:
        my_phone_book.add_contact(contact)

    my_phone_book.print_book()
    my_phone_book.delete_contact("+71234567809")
    my_phone_book.find_favourite()
    my_phone_book.find_contact('Mary Lee')
