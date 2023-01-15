def laps_to_miles(number_of_laps):
    return number_of_laps*0.25

if __name__ == "__main__":
    import time
    UsersLaps = ""
    while True:
        try:
            UsersInput = float(input("Enter how many laps you ran today\n"))
            UsersLaps = UsersInput
            break
        except ValueError:
            print("Unable to process your request dude!!")
            time.sleep(1)

    print(f"That means you ran:")
    time.sleep(1)
    print(laps_to_miles(UsersLaps),"miles!")
