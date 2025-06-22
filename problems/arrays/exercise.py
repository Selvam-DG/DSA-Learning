######### EXERCISE 1 ################

#Create a list to store these monthly expenses and using that find out
expenses = [2200, 2350, 2600, 2130, 2190]
# 1.  In Feb, how many dollars you spent extra compare to January?
extra_spent = expenses[1] - expenses[0]
print(" In Feb,  dollars spent extra compare to January: ", extra_spent)

# Find out your total expense in first quarter (first three months) of the year.
first_quarter_expenses = expenses[0] + expenses[1] + expenses[2]
print('first quarter expenses: ',first_quarter_expenses)

# spent exactly 2000 in any month
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print('Month: ',i+1)

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses[5] = 1980

#You returned an item that you bought in a month of April andgot a refund of 200$. Make a correction to your monthly expense listbased on this
expenses[3] = expenses[3]-200