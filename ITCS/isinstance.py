print("We can use the 'isInstance' keyword to check the datatype of a variable. \n")

print("Let's create a variable and initialise it, then check its type. \n")

num3 = 46

print("We've created a new variable called num3, and set its value to "
      + str(num3) + ". \n")

check = isinstance(46, str)

print("We've created a new variable called 'check', "
      + "and initialised its value to an isinstance check, "
      + "which will return " + str(check) + ", "
      + "because the isinstance check is checking to see if 46 is a string. \n")

print("Use the isinstance keyword to check if "
      + "a variable is of a specific datatype. \n")

print(isinstance(3.5, int))

print(isinstance(57, float))

print(isinstance("a string", str))
