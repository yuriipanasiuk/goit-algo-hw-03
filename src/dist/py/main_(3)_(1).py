def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            read_salary = [el.strip() for el in file.readlines()]
            total = 0
            number_of_developers = len(read_salary)

            for el in read_salary:
                _, salary = el.split(',')
                total += float(salary)

            average = total / number_of_developers

            return total, average

    except FileNotFoundError:
        print (f'File with {path} not found')
        return 0, 0
    
    except ValueError:
        print(f'Developer salary not found')
        return 0, 0


total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")