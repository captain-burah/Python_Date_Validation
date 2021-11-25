d = int(input("Enter Date: "))
m = int(input("Enter Month: "))
y = int(input("Enter year: "))

if ((y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) and
    1 <= m <=12 and
    1 <= d <= 31):
    if (m == 2 and 1 <= d <= 29):
        output = "Date is valid"
    elif ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and (1 <= d <= 31)):
        output = "Date is valid"
    elif ((m == 4 or m == 6 or m == 9 or m == 11) and (1 <= d <= 30)):
        output = "Date is valid"
    else:
        output = "Date is invalid"
        
elif (y % 400 != 0 or (y % 4 != 0 and y % 100 == 0) and
    1 <= m <=12 and
    1 <= d <= 31):
    if (m == 2 and 1 <= d <= 28):
        output = "Date is valid"
    elif ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and (1 <= d <= 31)):
        output = "Date is valid"
    elif ((m == 4 or m == 6 or m == 9 or m == 11) and (1 <= d <= 30)):
        output = "Date is valid"
    else:
        output = "Date is invalid"
else:
    output = "Date is invalid"
    
if (output == "Date is valid"):
    if (m == 2 and d == 29):
        d = 1
        m+=1
    elif (d == 31 and m == 12):
        d = 1
        m = 1
        y+=1
    elif (d == 31 and m < 12):
        d = 1
        m+=1
    elif ((m == 4 or m == 6 or m == 9 or m == 11) and d == 30):
        d = 1
        m+=1
    else:
        d+=1
    print(output)
    print("Next Date is: "+str(d)+"-"+str(m)+"-"+str(y))
else:
    print(output)
    
    
