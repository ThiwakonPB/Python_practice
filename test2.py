
while True :
    f = float(input("Enter celcius"))
    r = float((f-32)/1.8)
    print(r)
    ans = int(input("would you like to re-try? 1: Yes any other number: No"))
    if (ans == 1):
        print("retry")
    else :
        print("end")
        break