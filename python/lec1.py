Time = int(input("Enter time in second:"))
if(Time < 0):
    print("enter popsitive number")
elif(Time< 3600):
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{min} min :{sec}sec")
else:
    hour = Time//3600
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{hour} hours: {min} min: {sec} second")

    