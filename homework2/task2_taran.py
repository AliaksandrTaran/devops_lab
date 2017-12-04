#!/usr/bin/python
def Square_Number():
    try:
        iter=input("Input number of iterations:")
    except :
        print("You must input intger!")
        exit(1)
    for i in range(iter):
        print(pow(i,2))

def Polindrom():
    word=raw_input("Inpit your string:")
    if( word[:]==word[::-1]):
        print("Your string is polindrom")
    else:
        print("Your string is not polindrom")

def System_of_calculation():
    try:
        numb=input("How many number would you like to see?\n")
    except:
        print("You must input intger!")
        exit("Bad input")
    for i in range(numb):
        print "%s\t\t\t%s\t\t\t%s\t\t\t\t%s" % (i+1, (oct(i+1)[1:]), (hex(i+1)[2:]), (bin(i+1)[2:]))


def Reverse_String():
    str_for_revers=raw_input("Input string to reverse\n")
    str_for_revers=' '.join(word[::-1] for word in str_for_revers.split())
    print(str_for_revers)


def Sets():
    try:
        number = raw_input("Input size of array and set :\n").split()
        array_size, set_size = int(number[0]), (number[1])
    except:
        print("You should enter 2 numbers trough the whitespace")
        exit(1)
    try:
        set1 = raw_input("Input " + str(set_size) + " numbers for set1:\n").split()
    except:
        print("You should enter" + str(set_size) + " numbers trough the whitespace")
        exit(1)
    try:
        set2 = raw_input("Input " + str(set_size) + " numbers for set2:\n").split()
    except:
        print("You should enter" + str(set_size) + " numbers trough the whitespace")
        exit(1)
    try:
        mas = raw_input("Input " + str(array_size) + " numbers for massive:\n").split()
    except:
        print("You should enter " + str(array_size) + " numbers trough the whitespace")
        exit(1)
    print(sum([(x in set1) - (x in set2) for x in mas]))


def Squares():
    try:
        h = int(raw_input("Input h:\n"))
    except:
        print("Enter int number")
        exit(1)
    try:
        w = int(raw_input("Input w:\n"))
    except:
        print("Enter int number")
        exit(1)
    try:
        n = int(raw_input("Input number of rectangles:\n"))
    except:
        print("Enter int number")
        exit(1)
    pict = [[0] * w for i in range(h)]
    print(pict)
    for i in range(n):
        try:
            x1 = int(raw_input("Input x1:\n"))
        except:
            print("Enter int number")
            exit(1)
        try:
            x2 = int(raw_input("Input x2:\n"))
        except:
            print("Enter int number")
            exit(1)
        y1 = x1
        y2 = x2
        if (x1 > x2):
            x = x1;
            x1 = x2;
            x2 = x;
        if (y1 > y2):
            y = y1;
            y1 = y2;
            y2 = y;

        k = x1 - 1
        l = y1 - 1
        while (k < x2):
            while (l < y2):
                pict[k][l] = 1
                l += 1
            l = y1 - 1
            k += 1
    counter = 0
    for i in range(h):
        for j in range(w):
            if pict[i][j] == 0:
                counter += 1
    print("\n"+str(counter))






if __name__ == '__main__':
   while(True):
        print("\n\nChoose task:\n1\tSquare_Number\n2\tPolindrom\n3\tSquares\n4\tSystem of calculation\n5\tSets\n6\tReverse string\n0\tExit")
        try:
            choice=input("")
        except :
            print("You must input intger!")
            continue;
        if(choice==1):
            Square_Number()
        elif(choice==2):
            Polindrom()
        elif(choice==3):
            Squares()
        elif(choice==4):
            System_of_calculation()
        elif(choice==5):
            Sets()
        elif(choice==6):
            Reverse_String()
        elif(choice==0):
            exit("Goodbye!")
        else:
            print("You enter wrong number")
            continue
