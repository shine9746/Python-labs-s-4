#Python programme to print sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum(n):
     
      if n < 1:
        return 0

      else:
        return  (n+sum(n-2))

input = int(input("Enter a number : "))

print("Sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) is : \n ",sum(input))
