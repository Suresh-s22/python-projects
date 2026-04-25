'''def count(n):
    d_cnt=0
    while n>0:
        n=n//10
        d_cnt+=1
    return d_cnt
def sumofdigitcnt(n,p):
    s=0
    while n>0:
        d=n%10
        s+=d**p
        n=n//10
    return s
def armstrong(num):
    d_cnt=count(num)
    s=sumofdigitcnt(num,d_cnt)
    if s == num:
        return True
    else:
        return False
res=armstrong(153)
print(res)

'''

class Count:
    def __init__(self,n):
        self.n = n
        cnt = 0
        temp = n
        while temp > 0:
            temp = temp//10
            cnt+=1
        self.count=cnt
    def __str__(self):
        return f"digit count: {self.count}"
c1=Count(123495)
print(c1)
        
        



