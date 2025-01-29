sum = 0
n = int(input("Enter Number Of Students: "))
for i in range(0,n):
    name = int(input("Enter Marks: "))
    sum = sum + name
print("Total Marks: %d"%(sum))
print("Mean: %.2f"%(sum/n))

    
