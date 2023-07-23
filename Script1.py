#Products and prices

apples = str("$1ea")
eggs = str("$0.25ea")
bread = str("$2.50ea")
meat = str("$10/lbs")
orangeJuice = str("$2/litre")

#Customer inputs price #Argument inputs az floats after

q_of_apples = int(input("How many apples do you wish to purchase today?") * 1)
qq_of_eggs = int(input("How many eggs do you wish to purchase today?"))
q_of_eggs = float(qq_of_eggs) * 0.25
qq_of_bread = int(input("How many bread do you wish to purchase today?"))
q_of_bread = float(qq_of_bread) * 2.50
libs_of_meat = int(input("How much meat do you wish to purchase today?") * 10)
q_of_orange_juice = int(input("How many Orange Juice do you wish to purchase today?") * 2)

sales_tax = 0.13
#sub_total = q_of_apples + q_of_eggs + q_of_bread + libs_of_meat + q_of_orange_juice
sub_total = q_of_apples + q_of_eggs + q_of_bread + libs_of_meat + q_of_orange_juice
total_sales_tax = sub_total * sales_tax
amount_to_pay = sub_total + total_sales_tax

#Purchased prices each product to be displayed to the customer

print("Apples: $", q_of_apples)
print("Eggs: $", q_of_eggs)
print("Apples: $", q_of_bread)
print("Meat: $", libs_of_meat)
print("Orange Juice: $", q_of_orange_juice)
print("Your sub_total is: $", sub_total)
print("Tax: $", total_sales_tax)
print("Your total amount to pay is: $", amount_to_pay)

print("Thank you!")


