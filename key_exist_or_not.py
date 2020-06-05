#5.check whether a key is exists in dictionary or not

Dict={"a":"Benz","b":"BMW","c":"maruthi","d":"ford"}
key=input("Enter the key to check whether it is present in Dictionary or not: ")


#Method-1

if key in Dict.keys():
    print("Exist")
else:
    print("Not Exist")


#Method-2
    
key_list=list(Dict.keys())
exist_count=0
for i in range(0,len(key_list)):
    if key==(key_list[i]):
        print("Exist")
        exist_count+=1
if exist_count==0:
    print("Not Exist")


#Method-3
    
if key in Dict:
    print("Exist")
else:
    print("Not Exist")


#Method-4

exist_count1=0    
for x in Dict:
    if key==x:
        print("Exist")
        exist_count1+=1
if exist_count1==0:
    print("Not Exist")


#Method-5

key_list=list(Dict.keys())
exist_count2=0
i=0
while(i<len(key_list)):
    if key==(key_list[i]):
        print("Exist")
        exist_count2+=1
    i+=1
if exist_count2==0:
    print("Not Exist")







    
