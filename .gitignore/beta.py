import math
c3=[]
c4=[]
c5=[]
hd=[]
n=int(input("Enter number of nodes: "))
k=int(input("Enter value of k: ")) #number of data streams or base stations

i=n
j=k

umax=math.floor(math.fabs(i)/j)
        
if(umax%2==0 and umax>=4):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            
            t=t1+t2
            
            nalpha=umax/2
            
elif(umax==2):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            
            t=t1+t2
            
elif(umax==3):
            t1=math.floor((2*(math.fabs(i)-umax)/(umax+1))+1)
            temp2=math.fabs(i)-(t1*((umax+1)/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            
            t=t1+t2
elif(umax%2!=0 and umax>=5):
            t1=math.floor((2*(math.fabs(i)-umax)/(umax+1))+1)
            temp2=math.fabs(i)-(t1*((umax+1)/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            
            t=t1+t2
           
            nalpha=(umax-3)/2
            
      

l=64
for i in range(1,k+1):
    l=l+1
    for j in range(1,t1+1):
        hd.append(chr(l)+str(j))
        cthree=int(math.fmod((3*(i-1)+2*(j-1)),n)+1)
        cfour=int(math.fmod((3*(i-1)+2*(j-1)+1),n)+1)
        cfive=int(math.fmod((3*(i-1)+2*(j-1)+2),n)+1)
        c3.append(cthree)
        c4.append(cfour)
        c5.append(cfive)
    c3.append('|')
    c4.append('|')
    c5.append('|')
    
print(hd)
print(c3)
print(c4)
print(c5)    


    

    


