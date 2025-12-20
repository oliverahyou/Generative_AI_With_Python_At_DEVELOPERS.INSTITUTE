#Exercise 1: Favorite Numbers
my_fav_numbers = {7, 10}
my_fav_numbers.remove(10)
print(my_fav_numbers)
friend_fav_numbers = {6, 9}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

#Exercise 2: Tuple
int_tup = (1, 2, 3)
print(int_tup)
#int_tup.add(5)
#print(int_tup)
#Reason: Some values remain constant, for example Date of Birth or Gender so using Tuple in this case can be more efficient when packing and unpacking large amounts of fixed values

#Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
no_of_apples = basket.count("Apples")
print(no_of_apples)
basket.clear()
print(basket)

#Exercise 4: Floats
#Recap: A float is an integer containing decimal values whereas an integer is a whole number from negative infinity to infinity
float_and_int = [ 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#loopformation
start_int = 1.0
while start_int <= 5:
    start_int += 0.5
    print(start_int)

