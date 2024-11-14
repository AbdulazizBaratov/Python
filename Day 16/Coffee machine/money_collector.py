overall = 0

def Money_coins():
    def UZS(overall):
        M_sum =int(input("Sum"))
        overall += M_sum
    def USD(overall):
        M_USD = (input("$"))
        overall += M_USD * 12000
    def EUR (overall):
        M_EUR = int(input("€"))
        overall += M_EUR * 13000
    def RUB(overall):
        M_RUB = int(input("₽"))
        overall += M_RUB * 150
    def KZT(overall):
        M_KZT = int(input("₸"))
        overall += M_KZT * 150
    print('''
-For insurting UZS (S)
-For insurting USD (D)
-For insurting RUB (R)
-For insurting KZT (T)
-For exiting (E)
''')
    def check():
        answer = input("").lower()
        if answer == "s":
            UZS(overall)
        elif answer == "d":
            USD(overall)
        elif answer == "r":
            RUB(overall)
        elif answer == "t":
            KZT(overall)
    check()
    # I have to add going beck when I Will have done bith main
    print(f"you have {overall} sums")
    a = input("do ypu wanna add more money?(Y/N)").lower()
    if a == "y":
        check()
    #I need to add use casse for "No"
Money_coins()