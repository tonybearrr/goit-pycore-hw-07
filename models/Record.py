from .Phone import Phone
from .Name import Name
from .Birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones) if self.phones else "no phones"
        bday = self.birthday if self.birthday else "no birthday"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {bday}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = Phone(new_phone)

        
    def delete_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        
    def find_phone(self, phone):
        for phone_number in self.phones:
            if phone_number.value == phone:
                return phone_number
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)