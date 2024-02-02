# if - if
# if else - if elif
# if else if

age=int(input("Enter your age: "))

# if (){

# }

"""Indentation is used for structuring the python program, just in the same way curly braces do in C++/Java"""

if age==18:
    print("First Time Voter")
elif age<18: # else if - elif
    print("Not eligible")
elif age>60:
    print("Senior Citizen")
else:
    print("Indian Citizen")

