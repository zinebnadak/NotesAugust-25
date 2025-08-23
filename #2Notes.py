#Now I will try something new. When I want to test if my code is runnable I don´t want to start from the beginning, I want to be able to run code from desired line - but  in Python you can´t directly start running a script from arbitrary line number!
#Instead I split my code into parts using infunctions like this, giving me similar experience. (or you can just test the code by copiying and pasting a snippet in the python console tab)

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

part1()