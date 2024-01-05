#산술연산자 +,-,*,/,//,%,** [수]
a=int(input())
if a==100:
    print('0 0')
else:
    b=a//10
    c=a%10
    print(b,c)

a=int(input())
a1=a//60
a2=a1//60
a3=a%60
print(f"{a2}시{a1}분{a3}초")

a=int(input())
b1=a//100
b2=b1%10
print(b2)

#비교연산자 >(초과),<(미만),>=(이상),<=(이하),==(같다),!=(다르다) [bool](TRUE OR FALSE)
print(3>1)
print(3<1)

#논리연산자 and(a 그리고 b), or(a 또는 b), not(a반대) [bool](TRUE OR FALSE)
#True(bool)출력예시
print(3>1 and 5>1)#전부 참
print(3>1 or 3<1 or 2<1)#하나라도 참
print(not(3<1))#반대

#할당연산자
a=3 #a=3
b=1
b+=3 #3더하기 b=4
b-=3 #3빼기 b=1
b*=3 #3곱하기 b=3
b/=3 #3나누기 b=1
print(b)