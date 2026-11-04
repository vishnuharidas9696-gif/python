y=int(input("Enter the final year"))
print("Future Leap Years From 2026:")
for i in range(2026,y+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)