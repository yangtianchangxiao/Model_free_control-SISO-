import random
import math
import numpy as np
def randset(n):
    h=[]
    while(n>0):
        h.append(float("%.2f" % random.uniform(0,2)))
        n=n-1
    return h
err=eval(input("input error"))
num=eval(input("input number of unit in single hidden layer"))
size=eval(input("the length of input sequence"))
xita=eval(input("input the rate of learning"))
extend=eval(input("input the time of extent"))
times=eval(input("input the times of circulation"))
err_list=[]
errZ_list=[]
output_list=[]
value_output=0

for i in range(size-1):
    err_list.append(err)
    errZ_list.append(err)
err_list.append(0)
errZ_list.append(0)
err_mean=sum(err_list)/size
err_sigema=np.std(err_list)

for i in range(size):
    errZ_list[i]=(err_list[i]-err_mean)/err_sigema

h=randset(num*size)
w=randset(num)

while(times>0):


    value_mid=[]
    for i in range(num):
        value_mid.append(0)
        for j in range(size):
            value_mid[i]=value_mid[i]+h[i*size+j]*errZ_list[j]
        value_mid[i]=value_mid[i]+1

        value_mid[i]=1/(1+math.exp(-1*value_mid[i]))
        value_output=value_mid[i]*w[i]+value_output
    value_output=value_output+1

    sum_w=sum(w)
    for i in range(num):
        w[i]=w[i]+xita*extend*value_mid[i]
        for j in range(size):
            h[i*size+j]=h[i*size+j]+xita*extend*err*value_mid[i]*(1-value_mid[i])*errZ_list[j]*sum_w
    output_list.append(value_output)
    print("This is {} times circulation".format(times))
    print("output is")
    print((value_output))
    print("err is")
    err=err-value_output+2*random.random()
    print(err)
    err_list=[err]+err_list[:-1]
    err_mean=sum(err_list)/size
    err_sigema=np.std(err_list)
    for i in range(size):
        errZ_list[i]=(err_list[i]-err_mean)/err_sigema  
    times=times-1

    

