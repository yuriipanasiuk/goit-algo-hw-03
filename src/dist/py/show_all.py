def show_all(contacts):
    contact_list=[]

    if not contacts:
        return 'Contacts list are empty'
    
    for name, phone in contacts.items():
        contact_list.append(f"{name}: {phone}")

    return "\n".join(contact_list)
