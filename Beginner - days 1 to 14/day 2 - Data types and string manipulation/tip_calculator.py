#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip calculator")
bill_total = float(input("What was the total bill?\t\t"))
tip_rate = float(input("How much tip would you like to give?\t"))
tip_rate = 1 + tip_rate/100
bill_split = int(input("How many people to split the bill?\t"))
split_bill = (bill_total/bill_split) * tip_rate
print(f"\nEach person should pay:\t\t\t{split_bill:.2f}")
