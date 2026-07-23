x = int(input("enter the marks obtained"))
if 90<=x<=100:
    print("Marks obtained: ",x)
    print("Grade is: A+")
    print("Remark : Outstanding")
    print("Result: Pass")
elif x>=75:
    print("Marks obtained: ",x)
    print("Grade is: A")
    print("Remark : Excellent")
    print("Result: Pass")
elif x>=60:
    print("Marks obtained: ",x)
    print("Grade is: B")
    print("Remark : Good")
    print("Result: Pass")
elif x>=50:
    print("Marks obtained: ",x)
    print("Grade is: C")
    print("Remark : Average")
    print("Result: Pass")
elif x>=40:
    print("Marks obtained: ",x)
    print("Grade is: D")
    print("Remark : Pass (Needs Improvement)")
    print("Result: Pass")
else:
    print("Marks obtained: ",x)
    print("Grade is: F")
    print("Remark : Fail")
    print("Result: Fail")
