
# Code Body
menu_intro = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""


appetizers = ['Appetizers', 'Wings', 'Cookies', 'Spring Rolls']
entrees = ['Entrees', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Desserts', 'Ice Cream', 'Cake', 'Pie']
whole_menu = appetizers + entrees + desserts
total_order = {}

order_intro = """
***********************************
** What would you like to order? **
***********************************
"""


def print_section(section):
    for item in section:
        if item == section[0]:
            print(item)
            dashes = ''
            for letter in item:
                dashes += '-'
            print(dashes)
        else:
            print(item)
    print('\n')


def take_order():
    while True:
      
        new_item = input('> ').title()

        print('\n')

        if new_item == 'Quit':
            break
          
        elif new_item not in whole_menu:
            print('** Sorry, but we don\'t make %s **' % new_item)
        elif new_item not in total_order:
            total_order[new_item] = 1
            print('** 1 order of %s has been added to your meal **' % new_item)
        elif total_order[new_item] >= 1:
            total_order[new_item] += 1
            print('** Another order of %s has been added **' % new_item)
            print('** That makes %s total **' % total_order[new_item])
          
        print('** Would you like anything else? **')
        print('\n')


print(menu_intro)
print_section(appetizers)
print_section(entrees)
print_section(desserts)
print(order_intro)
take_order()