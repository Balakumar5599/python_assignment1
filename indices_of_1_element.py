#4.Find the index of all 1 elements:-

inp_list=[1,2,4,5,1,1,4,1,56]
indices_list=[]
for i in range(0,len(inp_list)):
    if inp_list[i]==1:
        indices_list.append(i)
print("Indexes of 1 elements: ",indices_list)

#user input

inp_list=[int(x) for x in input().split(",")]
inp_list=list(inp_list)
indices_list=[]
for i in range(0,len(inp_list)):
    if inp_list[i]==1:
        indices_list.append(i)
print("Indexes of 1 elements: ",indices_list)
