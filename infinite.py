#How to understand ramanujan summation

print("The Ramanujan Summation: 1 + 2 + 3 + ⋯ + ∞ = -1/12?")

def translate(A):
    b =len(A) 
    for i in range(b):
        if ( i == b-1):
            print(A[i],end = "+... ")
        else:
            print(A[i],end = '+')

S = [1,2,3,4,5,6,7,8] # S=infinite array 1+2+3+4+5+...
S1  =  [1,-1, 1,-1, 1,-1, 1,-1,]
s1= 1/2
translate(S1)
print("= S1 Array")
print("S1 sum = 1 or 0 = 1+0/2 -> ", s1 ,"≌ 1/2\n")

S2  =  [1,-2, 3,-4, 5,-6, 7,-8]
translate(S2)
print("= S2 Array")
S20 =  [0, 1,-2, 3,-4, 5,-6,-7,8,-9]
#---> S2 + S2 =?
S2plusS20=[]
for i in range(len(S2)-1):
    result=S2[i]+S20[i]
    S2plusS20.append(result)
translate(S20)
print("\n")
translate(S2plusS20)
print("= S2 + S2 = 2*S2",)
s2=1/4
print("2*(S2)= 1/2 ===> S2 = ",s2 ,"≌ 1/4")

SminesS2 =[]
#---> S - S2 =?
for j in range(len(S)-1):
    rslt = S[j]-S2[j]
    SminesS2.append(rslt)
print("\nS: ", end = "")
translate(S)
print("\nS2:" , end ="")
translate(S2)
print("\nS - S2 =",SminesS2)
print("S - S2 = 4(1+2+3+4+5+...)")
print("S - S2 = 4*(S) \n-S2 = 3*(S) ===> -1/4 = 3*(S)")
P = translate(S)
s = -1/12
print(-s2/3, "= S ≌ -1/12\n")

print("✔️   The Ramanujan Summation: 1 + 2 + 3 + ⋯ + ∞ = -1/12 ✔️")
