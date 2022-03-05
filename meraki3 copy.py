# WITHOUT ARGUMENTS
def evenodd():
    a=int(input("enter a numnber"))
    if a%2==0:
        print("even")
    else:
        print("odd")
evenodd()

# WITH ARGUMENTS
def evenodd(a):
        if a%2==0:
                print("even")
        else:
                print("odd")
m=int(input("enter a number to check if it is even or odd"))

# ex
def attendance(name,status="absent"):
        print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh")