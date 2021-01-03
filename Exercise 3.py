#Gausses the number

gussed_no = 15
no_of_gusses = 5

while no_of_gusses >= 1:
    print("Guess the no :")
    num = int(input())
    if num == 15:
        print("Hurry You won:")
    elif num<=50 and num>=30:
        print("Please enter in the range of 1 to 30")
    elif num>=20 and num<=30:
        print("try in the range of 1 to 20 ")
    elif num>=1 and num <15:
        print("try in the range of 15 to 20")
    elif num>16 and num<=20:
        print("try in the range of 14 to 17")
    else: print("Invalid no:")
    no_of_gusses = no_of_gusses-1
    print("No of Guesses have left:", no_of_gusses)
