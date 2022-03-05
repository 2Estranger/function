# ex
def attendance(name,status="absent"):
        print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh")

# debug
def greet(*names):
        for name in names:
                print("Welcome", name)
greet("Rinki","Vishal","Kartik","Bijender")

# 2nd debug
def info(name,age="31"):
        print(name + " is " + age + " years old")
info("Sonu")
info("Sana", "17")
info("Umesh", "18")

# 3rd debug
def studentDetails(name,currentMilestone,mentorName):
        print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
studentDetails("Prena","loop","Rakhi")

# function questions 2
def function(name,histry):
        print("Hello my name is",name)
        print("i am",histry,"of Navgurukul")
function("Rishab","Co-founder")

# QUESTIONS 2 PART(1)
def students(*names):
        for name in names:
                print(name)        
students("Anju","Aarti","Vanshika","Soni","Zoya","manpreet")

# question part(2)
def is_greater_than_20(b,a="20"):
        print(b,"is greater than",a,"or not?")
        print(a,"is greater than,",b,"or not?")
is_greater_than_20("22","40")