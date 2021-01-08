# # Health Management System
# followuing features
# take the input from the three users (Hammad,Harry,Rohan) for the following function
# (log the file , retrive the file)
# Each client has 2 log file Diet and Exercise
# Write a function that takes the user input of the client's name. After the client's name is entered,
# it will display a message as "What you want to log- Diet or Exercise"
import datetime

def gettime():
    return datetime.datetime.now()


def user():
    print("Enter No of your name\n 1 :Hammad\n 2 :Harry\n 3 :Rohan")
    name = input(("Here:"))
    if name == '1':
        Hammad()
    elif name == '2':
        Harry()
    elif name =='3':
        Rohan()

    return name


def Hammad():
    log_in = input("Enter 1 for Diet: and 2 for Exercise:")
    if log_in == '1':
        action = input("What action do you want to perform Read or Write \n Press 'r' for read and 'w' for write:")
        if action =='r':
            f = open("Hammad food log.txt")
            print(f.read())
            f.close()
        elif action =='w':
            with open("Hammad food log.txt","a") as f:
                value = input("\nWrite what do you want to write:")
                f.write( value + "\n")

    if log_in =='2':
        with open("Hammad Exercise.txt") as f:
            print(f.read())

def Harry():
    log_in = input("Harry plz Enter 1 for Diet: and 2 for Exercise:")
    if log_in == '1':
        action = input("What action do you want to perform Read or Write \n Press 'r' for read and 'w' for write:")
        if action == 'r':
            f = open("Harry food log.txt")
            print(f.read())
            f.close()
        elif action == 'w':
            with open("Harry food log.txt", "a") as f:
                value = input("\nWrite what do you want to write:")
                f.write(value + "\n")

    if log_in == '2':
        action = input("What action do you want to perform Read or Write \n Press 'r' for read and 'w' for write:")
        if action == 'r':
            f = open("Harry Exercise.txt")
            print(f.read())
            f.close()
        elif action == 'w':
            with open("Harry Exercise.txt", "a") as f:
                value = input("\nWrite what do you want to write:")
                f.write(value + "\n")

def Rohan():
    log_in = input("Rohan plz Enter 1 for Diet: and 2 for Exercise:\n")
    if log_in == '1':
            action = input("What action do you want to perform Read or Write \n Press 'r' for read and 'w' for write:")
            if action == 'r':
                f = open("Rohan Food log.txt")
                print(f.read())
                f.close()
            elif action == 'w':
                with open("Rohan Food log.txt", "a") as f:
                    value = input("\nWrite what do you want to write:")
                    f.write(value + "\n")
    if log_in == '2':
        action = input("What action do you want to perform Read or Write \n Press 'r' for read and 'w' for write:\n")
        if action == 'r':
            f = open("Rohan Exercise.txt")
            print(f.read())
            f.close()
        elif action == 'w':
            with open("Rohan Exercise.txt", "a") as f:
                value = input("\nWrite what do you want to write:")
                f.write(value + "\n")



user()