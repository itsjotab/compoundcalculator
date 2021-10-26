starting_principal = int(input("Enter Starting Amount: "))
interest_rate = int(input("Interest amount: "))/100
length = int(input("Total days of compound: "))
nsp = starting_principal * (interest_rate + 1)
start = 1

while length >= start:
    print(start, round( nsp, 2))
    start += 1
    nsp = nsp * (interest_rate + 1)   
