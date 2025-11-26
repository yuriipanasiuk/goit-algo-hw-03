def get_cats_info(path):
    list_cats = []
    
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                part = line.strip().split(',')

                if len(part) == 3:
                    cat_info = {"id": part[0], "name": part[1], "age": part[2]}
                    list_cats.append(cat_info)
                else:
                    print(f'Incorect data in {line.strip()}')

        return list_cats

    except FileNotFoundError:
        print (f'File with {path} not found')
        return []

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
