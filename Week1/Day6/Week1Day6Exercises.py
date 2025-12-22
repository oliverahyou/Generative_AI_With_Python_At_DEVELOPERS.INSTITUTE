#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dictionary = dict(zip(keys, values))
print(my_dictionary)

#Exercise 2: Cinemax #2
family = {
    'rick': 43, 
    'beth': 13, 
    'morty': 5, 
    'summer': 8
}
Price_under_3 = 0 
Price_3_to_12 = 10
Price_over_12 = 15
total_price = 0
for name, age in family.items():
    if age < 3:
        total_price += Price_under_3
    elif 3 <= age <= 12:
        total_price += Price_3_to_12
    else:
        total_price += Price_over_12
print(f'The total price for the family is: ${total_price}')




#Exercise 3: Zara

#Exercise 4: Disney Characters

