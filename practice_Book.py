my_list = []
while len(my_list) != 7:  
  add_to_list = int(input('what is your token number:')) #here we are using int to convert anything
  # in the input to turn into a integer 
  #we are also using input statement so that we can get the input of the user
  my_list.append(add_to_list)
for i in range(len(my_list)):
  print(my_list[i])
# here we are using range function and length function first the len() function will detect how big is the list 
# then range function will convert that length number into range and we will be able to use it in our for loop
sorted_my_list = sorted(my_list)
print('this is the sorted version of your list: ', sorted_my_list)
#this is the sorted function it will sort the number or anything inside the list 