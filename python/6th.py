for i in range(1,6,2):
    print("%d"%i, end="")



for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬은 꿀잼입니다. ^^(i값:%d,k값:%d)"%(i,k))






hap, i=0,0

for i in range(1,101):
    if i % 3==0:
        continue

    hap+=i

print("1~100의 합계(3의 배수 제외):%d"%hap)









for i in range(1,51):
    print("*"*i)








i,k,guguline=0,0,""

for i in range(2,10):
    guguline=guguline+("# %d단 #"%i)
""
print(guguline)

for i in range(1,10):
    guguline=""
    for k in range(2,10):
        guguline=guguline+str("%2d * %2d= %2d" %(k,i,k*i))
    print(guguline)