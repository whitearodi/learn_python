
month = input("Enter the month: ")

# Improving functions 
# Define fn
#when checking a list use the `in` keyword 
def num_days(month):
    months_with_31_days = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
    months_with_30_days = ['apr', 'jun', 'sep', 'nov']

    if month in months_with_31_days:
         print(f'number of days in {month} is 31 days')
    elif month in months_with_30_days:
         print(f'number of days in {month} is 30 days')
    else: 
         print(f'number of days in {month} is 28 days ')


#Call the fn
num_days(month)