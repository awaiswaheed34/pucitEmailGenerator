sections = ["se" , "cs" , "it"]

def generateMorning(batch):
    for i in range(19 , 23):
        for j in range(0 , 53):
            rollNumber = str(j).zfill(3)
            print("b"+batch+"f"+str(i)+"m"+rollNumber+"@pucit.edu.pk" , end=",")
    

def generateAfternoon(batch):
    for i in range(19 , 21):
        for j in range(0 , 53):
            rollNumber = str(j).zfill(3)
            print("b"+batch+"f"+str(i)+"a"+rollNumber+"@pucit.edu.pk" , end=",")

for i in sections:
    generateMorning(i)
    generateAfternoon(i)
    print("\n\n\n\n\n\n")

