# Calculate SimpleIntrest
from tkinter import simpledialog


principalAmount = float(input('Enter the amount:'))
rateofIntrest = float(input('Enter the rateofinterest:'))
timeinYears = float(input('Enter the year:'))


# i wa s connfused what to take so i have taken float value

simpleInterest = (principalAmount*rateofIntrest*timeinYears)/100
print(simpleInterest)