#Now I will try something new. When I want to test if my code is runnable I don´t want to start from the beginning, I want to be able to run code from desired line - but  in Python you can´t directly start running a script from arbitrary line number!
#Instead I split my code into parts using functions like this, giving me similar experience. (or you can just test the code by copiying and pasting a snippet in the python console tab)

#def part1():
    #print("zineb")
    #pass

#def part2():
    #print("mamma")
    #pass

#part2()


#Program that calculates an items price, incl. tax.. The tax is in percent-format (%) and 25.5% of the items value. The result is printed in a neat way.
#Input only gives you strings unless you define them. float can handle both integers and decimals
def part1():
    price = float(input("Enter the price of the item (excl. tax):" ))
    tax_rate = 25.5 #in percent
    tax_amount = price * (tax_rate/100) #calculate tax amount and final price
    final_price = price + tax_amount

    print (f"Item price:      {price:.2f} €") #print result neatly
    print (f"Tax ({tax_rate}%):     {tax_amount:.2f} €")
    print (f"Total price (incl. tax)     {final_price:.2f} €")
    pass


#Program that reads the inserted number of seconds into a variable called "time". Input should be an Integer, representing total number of seconds. The program calculates how many hours,minutes and secondsthis corresponds to. Number of minutes and seconds should be only between 0-59.

def part2():
    time = int(input("Please, Insert the number of seconds:"))

    hours = time // 3600 # calculate hours, minutes and seconds
    remainder = time % 3600
    minutes = remainder // 60
    seconds = remainder % 60

    print (f"{time} seconds equals to {hours} hours, {minutes} minutes and {seconds} seconds.")#Print result

#Notes
#mathematical standard functions / built-in-functions
# x=max(a,b) or x=min(a,b)
# x=round(b,2) , to round of desired decimals
# x=abs (y)

#The "random" module
#random()
#uniform (a,b) gives random number between a<x<b
#randint (a,b) gives random integer number a<x<b
#shuffle (lis) shuffles the elements in the list lis
#sample (sek,n) gives a list with n numbers of random elements from sequence sek


def part3():

#Program of tossing two dices simultaniously:


#augmented assignment, is when we want to change a variables value
#i+=2 is the same as i=i+2

#assignment expression ":=" is used to assign the new value of an expression to variable, at the same time as calculating it.

#Python is an dynamically typed language :variables don´t have a fixed type. The type of the value a variable holds is determined at runtime. The type of x can change during the program.
# x= 5       x is an integer
# x= "hello"        x is now a string
# that is why in python the type of the variable can change
#annotations define type beforehand, what type is expected
#number: int = input ("write me a number: ")

#use typechecker pyright with command below, control if the types used in program correctly.
# > pyright filename.py
