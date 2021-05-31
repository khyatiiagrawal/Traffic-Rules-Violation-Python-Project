
import time

def hash_index(i):
    total=0
    for j in i:
        total+=ord(j)
    index=total%50    
    return index

def search_id(Id,d):
    item_index = hash_index(Id)
    try:
        print(f"the id {Id} has {d[item_index][Id]} number of criminal records")
    except:
        print("You have a clean record :)")

   

def initializeHash ():
    d =[{} for i in range(50)]
    return d

def insertHash (d, lic): 
    index=hash_index(lic)
    if lic in d[index].keys():
        d[index][lic] +=1
    else:
        d[index][lic] = 1


def printViolators (d):
    for i in d:
        for j,k in i.items():
            if k>=5:
                print(f"Alert! {j} lic number has violated rules.t5")
                with open("violators.txt","a") as f:
                    f.write(f"{j}, {k}\n")



def destroyHash (d):
    for _ in d:
        _ = {}


def main():

    print("WELCOME! TO PORTAL")
    time.sleep(2)
    driverhash=initializeHash()
    ans='y'
    while ans =='y':
        lic=input("Enter the License Number: \n")
        insertHash(driverhash,lic)  
        
        ans=input("Do you want to Enter again, Press y/n:\n ")
        if ans=='n':
            break

    printViolators(driverhash)

main()


    
        
