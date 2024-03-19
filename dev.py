items = {'coffee' : 7,
        'Pen' : 3,
        'Paper cup' : 2,
        'Milk' : 1,
        'Coke' : 4,
        'Book' : 5}
print('1.check inventory 2.incoming stock 3.outing stocks 4.exit')
a = True
while a :
    user_input = int(input('Enter Options: '))
    if user_input == 1:
        inventory = input('Enter name of product: ')
        if inventory in items:
            print(items[inventory])
    # incoming stocks
    if user_input == 2:
        key,value = input('Enter the name and quantity of product: ').split()
        value = int(value)
        if key not in items:
            new_incoming = {key : value}
            items.update(new_incoming)
            continue
        if key in items:
            items[key] += value
            continue
        # print(items)
    # outing stocks
    if user_input == 3:
        outing,quantity = input('Enter the name of product: ').split()
        quantity= quantity(int)
        if outing in items:
            items[outing] -= quantity
            continue
    # print(items)
    elif user_input == 4:
        print('Exiting Inventory')
        a = False
        break
        
    