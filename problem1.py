import datetime
name=input("Enter Your Name :")
age=int(input("Enter your age :"))
now = datetime.datetime.now()
print(name," you will turn 95 at",(95-age)+now.year)
