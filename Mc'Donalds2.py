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
  item_you_ordered = item_list[item-1]                                                                                                                                 
  return item_you_ordered
  print('item no:',item)                                      

car_in = input('are you in a car? yes or no ').lower()
while car_in == 'yes'   :
  welcome()  
  item_want = int(input('''Please state the item no. that you want:
  Cheeseburger - 1 
  Fries - 2
  soda - 3
  Ice cream - 4
  Cookie - 5 '''))  
  ordered_thing =get_item(item_want) 
  cart.append(ordered_thing)
  print('you have ordered ',cart)     
  car_in = input('do you wanna order more? yes or no ').lower()
print('your cart has:', cart)                                                            
print('thank you for being with us today.have a nice day!!')