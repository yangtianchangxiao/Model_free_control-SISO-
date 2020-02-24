import random
import math
def randset(n):
    h=[]
    while(n>0):
        h.append(float("%.2f" % random.uniform(0,10)))
        n=n-1
    return h
err=eval(input("input error"))
num=eval(input("input number of unit in single hidden layer"))
size=eval(input("the length of input sequence"))
xita=eval(input("input the rate of learning"))
extend=eval(input("input the time of extent"))
times=eval(input("input the times of circulation"))
err_list=[]
output_list=[]
value_output=0
while(times>0):
    for i in range(size):
        err_list.append(err)
    h=randset(num*size)
    w=randset(num)
    value_mid=[]
    for i in range(num):
        value_mid.append(0)
        for j in range(size):
            value_mid[i]=value_mid[i]+h[i*size+j]*err_list[j]
        value_mid[i]=value_mid[i]+1
        value_mid[i]=1/(1+math.exp(-1*value_mid[i]))
        value_output=value_mid[i]*w[i]+value_output
    value_output=value_output+1
    value_output=1/(1+math.exp(-value_output))
    sum_w=sum(w)
    for i in range(num):
        w[i]=w[i]+xita*extend*value_mid[i]
        for j in range(size):
            h[i*size+j]=xita*extend*err*value_mid[i]*(1-value_mid[i])*err_list[j]*sum_w
    output_list.append(value_output)
    print("This is {} times circulation".format(times))
    print((value_output))
    err=value_output+2*random.random()
    err_list=[err]+err_list[:-1]
    times=times-1

    

