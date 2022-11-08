def checkstateA(n):
 
    
    if(n[0]=='0'):
        stateB(n[1:])
 
    
    else:
        stateD(n[1:])
 
       
def stateB(n):
 
   
    if (len(n)== 0):
        print("string not accepted")
    else:   
     
        if(n[0]=='1'):
            stateC(n[1:])
 
        
        else:
            stateD(n[1:])
          

def stateC(n):
    print("String accepted")

def stateD(n):
    if (len(n)== 0):
        print("string not accepted")
    else:   
 
        
        if (n[0]=='1'):
            stateD(n[1:])
 
        
        else:
            stateE(n[1:])
  
def stateE(n):
    if (len(n)== 0):
        print("string not accepted")
    else:  
 
       
        if(n[0]=='0'):
            stateE(n[1:])
 
       
        else:
            stateF(n[1:])

def stateF(n):
    if(len(n)== 0):
        print("string accepred")
    else:
 
       
        if(n[0]=='1'):
            stateD(n[1:])
 
       
        else:
            stateE(n[1:])
      

if __name__ == "__main__":
    n = "0100101"
    checkstateA(n)