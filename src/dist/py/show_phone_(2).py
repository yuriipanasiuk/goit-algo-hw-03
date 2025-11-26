def show_phone(args, contacts):
    if len(args) != 1:
        return 'Please provide user name.'
    
    name = args[0]
    
    if contacts.get(name):
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f'Contact {name} not found in contacts list'