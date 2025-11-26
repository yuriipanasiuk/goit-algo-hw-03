from datetime import datetime

def get_days_from_today(date: str, format: str = '%Y-%m-%d') -> int | str:
   try:
       date_object = datetime.strptime(date, format)
       current_date = datetime.today()
       difference = current_date - date_object

       return difference.days
   except ValueError:
       return f'The date "{date}" does not match the expected format (YYYY-MM-DD)'

print(get_days_from_today('2025-10-07'))
