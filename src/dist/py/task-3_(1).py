import re

def normalize_phone(phone_number: str) -> str:
    normalize_number = re.sub(r'[^\d+]', '', phone_number)

    if normalize_number.startswith('+'):
        return normalize_number
    
    elif normalize_number.startswith('380'):
        return f'+{normalize_number}'
    
    return f'+38{normalize_number}'

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+12025550123",
    "+49123456789"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
