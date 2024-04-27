def add_contact(args:list, contacts:dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args:list, contacts:dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args:list, contacts:dict) -> str:
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    return "Contact not found."

def show_all() -> str:
    with open("contacts.txt", "r", encoding="utf-8") as file:
        return file.read()