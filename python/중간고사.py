x = 7.898989
print(int(x))

a=17//4
b=17%4
print(a,b)

a=input('숫자 입력:')
b= '200'
print(int(a)+int(b))

print('python','java',sep='-',end='!!!')
print('c++')

score = 85
if score >=90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
else:
    print('F')

s ='pythonprogramming' 
print(s[6:13])

data = [10,20,30]
data.append(40)
data.insert(1,15)
data.pop()
print(data)

x = 15
result = 'Pass' if x>=10 and x%2==1 else 'Fail'
print(result)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_squares=[x*2 for x in numbers if x % 2==0]
print(even_squares)