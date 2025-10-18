from decorators import input_error
from models.AddressBook import AddressBook
from models.Record import Record

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added"
    if phone:
        try:
            record.add_phone(phone)
        except ValueError as e:
            return str(e)
    return message

@input_error
def update_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    try:
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for {name} updated from {old_phone} to {new_phone}."
    except ValueError as e:
        return str(e)
    
@input_error 
def get_all_contacts(book: AddressBook):
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())
    
@input_error   
def get_one_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    phones = "; ".join(p.value for p in record.phones) if record.phones else "no phones"
    return f"{name}: {phones}"
    
@input_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    book.delete(name)
    return f"Contact '{name}' deleted."

@input_error
def add_birthday(args, book: AddressBook):
    name, bday, *_ = args
    record = book.find(name)
    record.add_birthday(bday)
    return f"Birthday added for {name}: {bday}"

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record.birthday:
        return f"{name}'s birthday is {record.birthday}"
    return f"{name} has no birthday set."

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    lines = [f"{name}: {bday}" for name, bday in upcoming]
    return "\n".join(lines)