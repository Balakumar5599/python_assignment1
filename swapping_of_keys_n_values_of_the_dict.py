#6.swapping of keys and values of the dictionary

inp_dict={21:"FTP",22:"SSH",23:"telnet",80:"http"}
output_dict={}


#method-1


for key,value in inp_dict.items():
    output_dict[value]=key
print(output_dict)

print()
#method-2


swap_dict={value:key for key,value in inp_dict.items()}
print(swap_dict)


print()
print("If you want to swap a keys and values of the user input dictionary")
print("Then enter the keys and values of the user dictionary")
print()

#method-3(user input)


key=[int(x) for x in input("Enter the keys: ").split()]
value=input("Enter the values: ").split(" ")
key_list=[]
value_list=[]
for i in key:
    key_list.append(i)
original_dict={}
swap_dict={}
for i in range(0,len(value)):
    original_dict[key_list[i]]=value[i]
print(original_dict)
for key,value in original_dict.items():
    swap_dict[value]=key
print(swap_dict)

