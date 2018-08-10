age = int(input('Enter your age: '))
age_seconds = age *365*24*60*60
print("You have lived for {seconds} seconds. This corresponds to {years} years.".format(seconds=age_seconds,years=age))
