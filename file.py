num1 = 42 #variable declaration, add value
num2 = 2.3 #variable declaration, add value
boolean = True #variable declaration
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialze list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) #access tuple value
print(pizza_toppings[1]) #access list value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #access dictionary value
person['name'] = 'George' #change dictionary value
person['eye_color'] = 'blue' #- NameError: name <variable name> is not defined
print(fruit[2]) #access tuble value

if num1 > 45: #conditional if statement
    print("It's greater")
else: #conditional else statement
    print("It's lower")

if len(string) < 5: #conditional if, length check
    print("It's a short word!")
elif len(string) > 15: #conditional else if, length check
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for loop start
    print(x)
for x in range(2,5): #for loop sequence
    print(x)
for x in range(2,10,3): #for loop sequence
    print(x)
x = 0 #variable declaration, add value
while(x < 5): #while loop start
    print(x) 
    x += 1 #while loop, increment

pizza_toppings.pop()- #AttributeError: 'tuple' object has no attribute 'pop'
pizza_toppings.pop(1) #TypeError: 'tuple' object does not support item assignment

print(person)
person.pop('eye_color') #AttributeError: 'tuple' object has no attribute 'pop'
print(person) #TypeError: 'tuple' object does not support item assignment

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if conditional
        continue #for loop continue
    print('After 1st if statement')
    if topping == 'Olives': #if conditional
        break #for loop breal

def print_hello_ten_times(): #function parameter
    for num in range(10): #function argument
        print('Hello')

print_hello_ten_times() #KeyError: 'favorite_team'

def print_hello_x_times(x): #function parameter
    for num in range(x): #function argument
        print('Hello')

print_hello_x_times(4) #NameError: name <variable name> is not defined

def print_hello_x_or_ten_times(x = 10): #function parameter
    for num in range(x): #function argument
        print('Hello')

print_hello_x_or_ten_times() #function return
print_hello_x_or_ten_times(4) #function return


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)