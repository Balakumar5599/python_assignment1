#2.To make a full URL from tuple items

#Method-1


url_tupitem=('www','hackkerrank','com','domains','python')
outp_url="https://"
ref_count=0
for items in url_tupitem:
    outp_url=outp_url+items
    if ref_count<2:
        outp_url=outp_url+'.'
    if ref_count>=2:
        outp_url=outp_url+'/'
    ref_count+=1
print("Output URL: ",outp_url)
print()


#Method-2 user input


user_inp=input("Enter the tuple elements: ").split(",")
tup_list=[]
outp_url1="https://"
ref_count1=0
print()
for items in user_inp:
    tup_list.append(items)
url_tupitem1=tuple(tup_list)
print("URL Tuple items are: ",url_tupitem1)
print()
for items in url_tupitem1:
    outp_url1=outp_url1+items
    if ref_count1<2:
        outp_url1=outp_url1+'.'
    if ref_count1>=2:
        outp_url1=outp_url1+'/'
    ref_count1+=1
print("Output URL: ",outp_url1)


