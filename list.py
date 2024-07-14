#Using a list 
 
sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

add_day = input("Add no of lemonades sold: ")
sales_w2.append(int(add_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
sales.sort()
worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5 
print(f'Worst day profit: {worst_day}')
print(f'Best day profit: {best_day}')
print(f'Combine: {worst_day} + {best_day}')