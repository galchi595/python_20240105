a=1 #int
b=3.21#float
c='ㅇ'#str
d=True#bool[True or False]
e=False#bool[True or False]

#bool() 불화
print(bool(a))
print(bool(0))
print(bool(""))

#list[]
coffee=['아이스','핫','라떼','믹스'] #[index]
bus_num=[10,9,8,7,6,5,4,3,2,1]
#리스트 안에는 어느 타입이나 다 ok
print(coffee[1])

mega_study=[[1,3,5],[5,6,7],[1,5,9]]
ae,af=map(int,input().split( ))
print(mega_study[ae][af])

#list() 리스트화
#numlist=list(1,2,3,4,5)#정수 리스트화 불가능
m=list("megastudy")#문자열 가능
print(m)

