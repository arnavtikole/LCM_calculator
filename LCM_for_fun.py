num_list=[]
numbers=int(input('enter a number: '))
num_list.append(numbers)
numbers_2=int(input('enter another number: '))
num_list.append(numbers_2)
ask=input('would you like to add another one? (Y/N) ')
while ask!='N':
    if ask=='Y':
        number_3=int(input('enter a number: '))
        num_list.append(number_3)
        ask=input('would you like to add another one? (Y/N) ')
    elif ask=='N':
        print('Thank You!')
#biggest number: 
biggest=max(num_list)
#product:
product=1
if ask=='N':
    for j in num_list:
        product=product*j
    for i in range(biggest,(product+1)):
        if all(i % num == 0 for num in num_list ):
            print(i,'is the LCM of',num_list)
            break
