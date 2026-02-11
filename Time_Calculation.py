def min_to_hour(minute):
    return minute / 60

def hour_to_min(hour):
    return hour * 60

def sec_to_min(second):
    return second / 60

def min_to_sec(minute):
    return minute * 60

def sec_to_hour(second):
    return second / 3600

def hour_to_sec(hour):
    return hour * 3600


while True:
    print("\nFS-Time Calculation")
    print("0. EXIT")
    print("1. Hour -> Minute")
    print("2. Hour -> Second")
    print("3. Minute -> Hour")
    print("4. Minute -> Second")
    print("5. Second -> Hour")
    print("6. Second -> Minute")

    choice = int(input("Enter The Choice: "))

    if choice == 0:
        print("Program Terminated")
        break

    elif choice == 1:
        hour = float(input("Enter Hour: "))
        print("Hour -> Minute =", hour_to_min(hour), "minutes")

    elif choice == 2:
        hour = float(input("Enter Hour: "))
        print("Hour -> Second =", hour_to_sec(hour), "seconds")

    elif choice == 3:
        minute = float(input("Enter Minute: "))
        print("Minute -> Hour =", min_to_hour(minute), "hours")

    elif choice == 4:
        minute = float(input("Enter Minute: "))
        print("Minute -> Second =", min_to_sec(minute), "seconds")

    elif choice == 5:
        second = float(input("Enter Second: "))
        print("Second -> Hour =", sec_to_hour(second), "hours")

    elif choice == 6:
        second = float(input("Enter Second: "))
        print("Second -> Minute =", sec_to_min(second), "minutes")

    else:
        print("Invalid Choice")
