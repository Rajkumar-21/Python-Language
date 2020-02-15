""""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

""""

import datetime

today=datetime.datetime.today()

print("Current time and date :")

print(today.strftime("%Y -%m -%d %H:%m:%s"))