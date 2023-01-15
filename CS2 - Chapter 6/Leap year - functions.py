def days_in_feb(year):
    if year %4 != 0:
        return 28
    elif year % 100 == 0:
        if year % 400 != 0:
            return 28
        return 29
    else:
        return 29

if __name__=="__main__":
    UsersYear = int(input("Please enter your year\n"))
    print(f"{UsersYear} Has {days_in_feb(UsersYear)} days in February")
