#----> ways to calculate pi , π=3,141592653589793238462643383

#One of the most well known and beautiful ways to calculate Pi (π) is to use the Gregory-Leibniz Series:
#Another series which converges more quickly is the Nilakantha Series which was developed in the 15th century. Converges more quickly 
# means that you need to work out fewer terms for your answer to become closer to Pi (π) .


#Gregory-Leibniz Series:
#π/4 =1 - 1/3 + 1/5 -1/7 + 1/9 - ... 
pi = 1
k=0
x=10**5
for j in range(3,x,2):
    if(k==0):
        pi -=1/j
        k=1
    else:
        pi +=1/j
        k=0
print("Greogry-Leibniz Series:π: " ,4*pi)


#Nilakantha Series: 
#π = 3+ 4/2*3*4 - 4/4*5*6 + 4/6*7*8 - 4/8*9*10 + ...
pi2=3
k=0
x=10**5
for m in range(2,x,2):
    if(k==0):
        pi2 += 4/(m*(m+1)*(m+2))
        k=1
    else:
        pi2 -= 4/(m*(m+1)*(m+2))
        k=0

print("Nilakantha Series:π: ", pi2)

#Mathematicians have also found other more efficient series for calculating Pi (π). Computer programs can add up more and more terms, 
#calculating Pi (π) to extraordinary degrees of accuracy. In 2014 the world record was that a computer has calculated Pi (π) correct 
#to 13,300,000,000,000 decimal places.