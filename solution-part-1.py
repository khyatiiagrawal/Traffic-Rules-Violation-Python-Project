

class PoliceNode:
    def __init__(policeRoot,policeID,fineAmt):
        policeRoot.policeID= policeID
        policeRoot.fineAmt = fineAmt
        policeRoot.bookingCount = 1
        policeRoot.left = None
        policeRoot.right = None
        
    def insertByPoliceId (policeRoot, newpoliceId, newamount):
        if policeRoot == None:
            return PoliceNode(policeRoot, newpoliceId,newamount)
        else:
            if newpoliceId < policeRoot.policeID:
                if policeRoot.left == None:
                    policeRoot.left = PoliceNode(newpoliceId,newamount)
                else:
                    policeRoot.left.insertByPoliceId(newpoliceId,newamount)
            elif newpoliceId > policeRoot.policeID:
                if policeRoot.right==None:
                    policeRoot.right=PoliceNode(newpoliceId,newamount)
                else:
                    policeRoot.right.insertByPoliceId(newpoliceId,newamount)
            elif newpoliceId==policeRoot.policeID:
                policeRoot.fineAmt+=newamount
                policeRoot.bookingCount+=1
            

    def printtree(policeRoot):
        if policeRoot.left:
            policeRoot.left.printtree()
        print(policeRoot.policeID,"-",policeRoot.fineAmt)
        
        print("bookingCount=",policeRoot.bookingCount)
        if policeRoot.right:
            policeRoot.right.printtree()

        
    def reorderPoliceTree (policeRoot):
        if self is not None:
            reorderPoliceTree(self.left, targetTree)
            targetTree = insertByBookingCount(targetTree, self.policeId,self.fineAmt,self.bookingCount)
            reorderPoliceTree(self.right, targetTree)
            self = None
        return self, targetTree
        

    def printPolicemen (policeRoot):
        outfile = open("police.txt", 'w')
        printPolicemenIntoFile(self, outfile)
        outfile.close()
        

    def printTopTen(policeRoot):
        outfile = open("policeTop10.txt", 'w')
        printTopTenIntoFile(self, outfile)
        outfile.close()
        
        listA = []
        infile = open("policeTop10.txt", "r")
        listA =  infile.readlines()
        infile.close()
        
        if len(listA) > 10:
            outfile = open("policeTop10.txt\", 'w')
            for i in range(0,10):
                outfile.write(listA[i])
            outfile.close()

    def destroyPoliceTree (policeRoot): 
        if self is None:
            return

        destroyPoliceTree(self.left)
        destroyPoliceTree(self.right)
        self = None

    def printPoliceTree (policeRoot):
         if self is None:
            return



with open("inputPS11.txt","r")  as f:
    count=0
    for _ in f:
        l = _.strip().split("/")
        policeId = int(l[0])
        liscence = l[1]
        amount = int(l[2])
        count+=1

        if count==1:
            data=PoliceNode(policeId,amount)
        else:
            data.insertByPoliceId(policeId,amount)

data.printtree()

print(data.fineAmt)

# d=PoliceNode(111,50)
# d.insertByPoliceId(222,40)
# d.insertByPoliceId(111,60)
# d.insertByPoliceId(333,70)
# d.insertByPoliceId(222,80)
# d.printtree()

