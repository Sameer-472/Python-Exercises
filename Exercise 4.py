# Astro star program



a = int(input("Enter no of rows:"))
b = bool(int(input("Entr 1 for True and 0 for False:")))

def star(a,b):
    c = 1

    if b == True:
        while c <= a:
            print(c*"*")
            c = c+1
    else:
            while a > 0:
                print(a*"*")
                a = a-1

star(a,b)