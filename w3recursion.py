
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\nRecursion Example Results")
# tri_recursion(6)

# def demo():
#   def demo():
#     print("prena")
#     print("rai")
#     demo1()
# def demo1():
#     print("antra")
#     print("rai")
#     demo()
# demo1()

# def demo():
#     print("prena")
#     demo()
# demo()


def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
n=int(input("Enter a numbre:"))        
print(sum(n))