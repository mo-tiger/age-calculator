from datetime import date
to = date.today()
year = int(input('Please Enter The Year Of Birth : '))
month = int(input('Please Enter The Month Of Birth : '))
day = int(input('Please Enter The day Of Birth : '))
print('Your Date Of Birth Is',day,'/',month,'/',year)
year1 =to.year - year
month1 = to.month - month
day1 = to.day - day
print('Your age is {} years {} month and {} days'.format(year1,month1,day1))
