cart = []
item_list = ('Cheeseburger ',
'Fries',
'soda ',
'Ice cream ',
'Cookie ')


def welcome():
  print('Welcome to Mc\'Donalds',' para pa pa pa!!')
  print('thank you for being with us today. What can i get for you today?')
  pass


def get_item(item):
  print('item no:',item)
  item_want = int(input('''Please state the item no. that you want:
  Cheeseburger - 1 
  Fries - 2
  soda - 3
  Ice cream - 4
  Cookie - 5 '''))
  how_much = int(input('how much quantity do you want of this item: '))
  item_selected = item_list[item_want-1]
  add_cart = (how_much,item_selected)                                                                 
  return add_cart


car_in = input('are you in a car? yes or no ').lower()
while car_in == 'yes'   :
  welcome()
  quantity_item = int(input('how many items do you want to order?'))
  for i in range(0,quantity_item):          
     item_added = get_item(i+1)
     cart.append(item_added)
  car_in = input('do you wanna order more? yes or no ').lower()
print('you have ordered these Items :', cart)
print('thank you for being with us today.have a nice day!!')