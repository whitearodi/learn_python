#Handling errors in pyhton we used the try except block
try:
   num = int(input("Enter a number"))
 
#except ValueError, ZeroDivisionError
except:
    print("Invalid input")
else:
      print("30 divided by", num, "is:", 30/num)
finally:
    print("**Thank you for playing**")
# try
#    # code u want to run
# except 
#    # executed if errors occurs 
# else
#    # executed if no error 
# finally
  #always executed 