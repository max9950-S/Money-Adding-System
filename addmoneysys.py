money = float(0)

def add(amt):
    global money
    money += float(amt)
    print(f"your new balance is: $", money, sep="")

q1 = input("Do you want $20?: ").lower()
if q1 == "yes":
    add(20)
if q1 == "no":
    print("ok")

q2 = input("Do you want $15?: ").lower()
if q2 == "yes":
    add(15)
if q2 == "no":
    print("ok")

interactive = input("how much money do you want?: ").lower()
add(float(interactive))
