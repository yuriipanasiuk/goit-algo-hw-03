import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
   if not (1 <= min <=max <= 1000 and quantity <= (max - min + 1)):
      return []
   
   random_numbers = random.sample(range(min, max + 1), quantity)
   random_numbers.sort()

   return random_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

