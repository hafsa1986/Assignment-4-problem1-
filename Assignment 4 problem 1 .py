#Problem 1: Current Date and Time 

import datetime

# current date and time
current = datetime.datetime.now()

print("Current Date and Time:", current)

# formatted version
formatted = current.strftime("%d-%b-%Y %I:%M %p")
print("Formatted Date and Time:", formatted)
