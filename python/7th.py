aa=[]
for i in range(0,4):
    aa.append(0)
hap=0

for i in range(0,4):
    aa[i]=int(input(str(1*1)+"번째 숫자:"))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계==>%d"%hap)






list1=[]
list2=[]
value=1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d"%list2[i][k],end="")
    print("")



inStr="<한글 python 프로그램>>"
outStr=""

for i in range(0,len(inStr)):
    if inStr[i]!='<' and inStr[i] != '>':
        outStr+=inStr[i]

print("원래 문자열==>"+'['+inStr+']')
print("공백 삭제 문자열==>"+'['+outStr+']')

