#1.Obtain the domain name from URL

#Method-1


url=input("Enter the the URL: ")
website=url.split('//')[1].split('/')[0]
domain_name=website.split('.')[-2]+'.'+website.split('.')[-1]
print("The Domain name from the URL is: ",domain_name)



#Method-2 [This method is searched in google and learned But we have to import tld 


from tld import get_tld
domain_name=get_tld(url, as_object=True)
print("The Domain name from the URL is: ",domain_name.fld)
