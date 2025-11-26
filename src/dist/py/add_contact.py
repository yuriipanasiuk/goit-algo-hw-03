def add_contact(args, contacts):
    if len(args) != 2:
        return 'Please provide both name and phone number.'
    
    name, phone = args
    contacts[name] = phone

    return "Contact added."