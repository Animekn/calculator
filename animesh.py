def addNumbers(numberA, numberB):
    return numberA + numberB
def subtractNumbers(numberA, numberB):
    return numberA - numberB

numberA = int(input("Enter a number: "))
numberB = int(input("Enter another number: "))
print("The sum of the two numbers is: ", addNumbers(numberA, numberB))
print("The difference of the two numbers is: ", subtractNumbers(numberA, numberB))