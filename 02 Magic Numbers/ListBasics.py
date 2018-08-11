numbers = [9,8,7,6,5,4,3,2,1,0]
print(numbers)
print("List length: {}".format(len(numbers)))
print("List element [0]: {}".format(numbers[0]))
print("List element [9]: {}".format(numbers[9]))

print("==Squares of 'numbers'==")
for number in numbers:
    print("          {}".format(number**2))
print("========================")

greater_than_three = 5>3
print("Five is greater than three: {}".format(greater_than_three))

equal_to_five = 6==5
print("Six is equal to five: {}".format(equal_to_five))


print("Five is less than five: {}".format(5<5))




return_string = ""
for number in numbers:
    if number > 5:
        return_string += "{} ".format(number)

print("\nAll numbers in list greater than 5: {}".format(return_string))


if not 3>5:
    print("\nThree is NOT greater than 5")

print(not True)
