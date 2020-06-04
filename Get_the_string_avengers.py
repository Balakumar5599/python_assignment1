#3.Get the string "avengers"


Given_list=["abc",[2,3,("xyz","the avengers")],1,2,3]
list1=list(Given_list[1])
extracted_list=list(list1[2])
output_string=str(extracted_list[1])
print(output_string[4:12])
