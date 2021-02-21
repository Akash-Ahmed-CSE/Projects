CRA=[]
AVG=[]
SGPA=[]
p=int(input("Enter number of semester:"))
for i in range(0,p):
    n = int(input("Enter number of subjects:"))

    for i in range(0, n):
        number=float(input("Enter GPA:"))
        cra=int(input("Enter Cradit:"))
        CRA.append(cra)
        ml=cra*number
        AVG.append(ml)

    s=sum(AVG)
    c=sum(CRA)
    sgpa=s/c
    s=0
    c=0
    AVG.clear()
    CRA.clear()
    print("SGPA :",sgpa)
    SGPA.append(sgpa)
x=sum(SGPA)
print("CGPA: ",x/p)




