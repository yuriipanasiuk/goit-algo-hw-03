def change_contact(args, contacts):
    if len(args) != 2:
        return 'Please provide both name and phone number.'
    
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    else:
        return f'Contact {name} not found in contacts list'