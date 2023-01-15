print("___**CALCULATOR** ___\n")
def main():
    try:    
        a=input("Enter a number : ")
        b=input("Enter a number : ")
        if "." in a:
            a = float(a)
        else:
            a = int(a)
        if "." in b:
            b = float(b)
        else:
            b = int(b)
    except Exception as e:
        print("...Please enter only digit not string....")
        
        
    print("")
    while True:
        def add():
            print("-"*25)
            print(f"Addition of {a}+{b} is = {a+b}")
            print("-"*25)

        def sub():
            print("-"*25)
            print(f"Subtraction of {a}-{b} is = {a-b}")
            print("-"*25)

        def mul():
            print("-"*25)
            print(f"Multiplication of {a}*{b} is = {a*b}")
            print("-"*25)

        def div():
            print("-"*25)
            print(f"Divition of {a}/{b} is = {a/b}")
            print("-"*25)

        n=int(input(" Press 1 for addition\n Press 2 for subtract\n Press 3 for multiply\n Press 4 for division\n Press 5 for New Numbers\n Press 6 for Quite\n Enter Your Choice :  "))
        if n==1:
            add()
        elif n==2:
            sub()
        elif n==3:
            mul()
        elif n==4:
            div()
        elif n==5:
            main()
        elif n==6:
            break
main()