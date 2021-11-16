name_1=input("what is your name:")
name_2=input("what is your name:")
name_3=input("what is your name:")

slices_in_the_pizza = input("how many slices in the pizza:")
price_of_pizza = input("what is the price of pizza: ")

percentage_1=input(name_1+" what percentage of the pizza you have ate:")
percentage_2=input(name_2+" what percentage of the pizza you have ate:")
percentage_3=input(name_3+" what percentage of the pizza you have ate:")

num_of_slices_ate_1=float(percentage_1)*float(slices_in_the_pizza)
num_of_slices_ate_2=float(percentage_2)*float(slices_in_the_pizza)
num_of_slices_ate_3=float(percentage_3)*float(slices_in_the_pizza)

price_of_1=float(percentage_1)*float(price_of_pizza)
price_of_2=float(percentage_2)*float(price_of_pizza)
price_of_3=float(percentage_3)*float(price_of_pizza)

print(name_1+" have ate "+str(num_of_slices_ate_1)+" slices and have payed "+str(price_of_1)+" $ for this meal")
print(name_2+" have ate "+str(num_of_slices_ate_2)+" slices and have payed "+str(price_of_2)+" $ for this meal")
print(name_3+" have ate "+str(num_of_slices_ate_3)+" slices and have payed "+str(price_of_3)+" $ for this meal")
