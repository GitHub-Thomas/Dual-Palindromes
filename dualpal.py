"""
ID:wzch_di3
TASK:dualpal
LANG:PYTHON3
"""
f1 = open("dualpal.in","r")
f2 = open("dualpal.out","w")
ans = f1.read()
index = ans.find(" ")
num = int(ans[0:index])
start = int(ans[index+1:len(ans)])
def radix(num,n):
    result = ""
    a = num
    while (a != 0):
        b = a // n
        c = a % n
        result = result + str(c)
        a = b
    return(result)

def judge(num):
    for i in range(0,len(num)//2):
        if (num[i] != num[len(num)-i-1]):
            return(0)
    return(1)

sum = 0

i = start + 1
while (sum !=num):
    a = judge(str(i))
    for j in range(2,10):
        radixans = radix(i,j)
        a = a + judge(radixans)
        if (a >= 2):
            sum = sum + 1
            f2.write(str(i)+'\n')
            break
    i = i + 1
f1.close()
f2.close()
