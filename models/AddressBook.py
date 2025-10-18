from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            record = self.data[name]
            del self.data[name]
            return record
        raise KeyError(f"Contact '{name}' not found")
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        result = []

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                days_until_birthday = (birthday_this_year - today).days
                
                if 0 <= days_until_birthday <= 7:
                    congratulation_date = birthday_this_year
                    
                    if birthday_this_year.weekday() >= 5:
                        days_until_monday = 7 - birthday_this_year.weekday()
                        congratulation_date = birthday_this_year + timedelta(days=days_until_monday)

                    result.append((record.name.value, congratulation_date.strftime("%d.%m.%Y")))
        return result