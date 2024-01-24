#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


# In[ ]:


usersD={'khaled':'123','khalil':'321'}
usersCountry={'khaled':'Egypt'}
userItemsCard=[]
userCashAmount=[]
#currentUser={'khaled':'123'}
currentUser=''





categories={'Shoes':[{'Canvas trainers':'649',
                     'Chukka boots':'1199',
                     'Chelsea boots':'1199',
                     'Hi-top trainers':'999',
                     'Leather sandals':'999',
                     'Leather trainers':'1499',
                     'Oxford shoes':'999',
                     'Soft slippers':'499',
                     'Pile-lined slippers':'399',
                     'Imitation suede driving shoes':'749'}],
            
          'Jeans':[{'Slim Jeans':'749',
                   'Slim Tapered Jeans':'749',
                   'Tapered Jeans':'749',
                   'Relaxed Tapered Pull-On Jeans':'749',
                   'Skinny Jeans':'749',
                   'Slim Straight Jeans':'749',
                   'Regular Jeans':'749',
                   'Tech Stretch Slim Jeans':'999'}],
            
          'Shirts':[{'Oxford shirt Regular fit':'499',
                    'Regular fit shirt':'649',
                    'Twill shirt jacket':'749',
                    'Corduroy shirt jacket':'749',
                    'Cotton flannel shirt':'499',
                    'Faux shearling-lined shacket':'899',
                    'Corduroy shacket':'649',
                    'Cotton denim shirt':'749',
                    'Easy-iron shirt Slim Fit':'349',
                    'Suede shacket':'1099'}],
            
          'T-shirts':[{'T-shirt with a motif':'199',
                     'Loose Fit Sports top':'349',
                     'Printed jersey top':'499',
                     'Raw-edge T-shirt':'299',
                     'Printed T-shirt':'449',
                     'Gilet Regular Fit':'649',
                     '2-pack Henley tops Slim Fit':'499',
                     'Cotton rugby shirt':'499',
                     'Long hooded T-shirt':'399',
                     'Waffled jersey top':'349'}],
            
            
          'Accessories':[{'Belt':'499',
                         'Rib-knit hat':'199',
                         'Running gloves':'349',
                         'Sports cap':'249',
                         '3-pack rings':'199',
                         'Braces':'249',
                         'Small shoulder bag':'499',
                         'Cotton canavas bag':'649',
                         'Pendant necklace':'199',
                         'Hat and scarf':'349',
                         'Felted wool hat':'499'}]}
          
            


# In[ ]:





# In[ ]:





# # WELCOME FUNCTION
# 

# In[ ]:


def welcomeF():
    print('Welcome to our store hope you enjoy our items :) <3 ')
    


# # Check if registered or not 

# In[ ]:


def checkifRegistered():
    flag=''
    flag=input('Are you already a member ? <yes/no>')
    if re.search(r'[yY]|[eE][sS]\s',flag):
            print('Welcome back sir \n')
            logIn()
    else:
            print('Would you please sign up first\n')
            register()
        


# In[ ]:





# # Login function

# In[ ]:


def logIn():
    global currentUser
    userid=input('Please Enter your ID to login : ').replace(" ","").lower()
    l=list(usersD.keys())
    for i in l:
        if userid == i:
            userpass=input("\nPlease Enter your password :").replace(" ","").lower()
            if userpass ==usersD[userid]:
                currentUser=userid
                print("{} Welcome To our store !!\n".format(userid))
                displayCategories()
            else:
                print("Your User id or password are not correct!! pls try again\n")
                logIn()
                
    print("Your User id or password are not correct!! pls try again\n")
    logIn()
                
                
            
    


# # Get user needed data to register
# 

# In[ ]:


def register():
    userid=input("\nPlease Enter your user id to register : ").replace(" ","").lower()
    if userid in usersD:
        print("this user id already a member!!\nif you forgot your user id or password pls call our office 123456\nif not pls try again\n")
        register()
    else:
        userpass=input("Please enter your password : ").replace(" ","").lower()
        usersD[userid]=userpass
        usercountry=input("Please Enter your current country : ").capitalize()
        usersCountry[userid]=usercountry
        print("Congrats!!!! you are a member now <3 \nEnjoy our store")
        logIn()
        
        


# In[ ]:





# # display categories and pic the items to buy
# 

# In[ ]:


def displayCategories():
    
    print('{}        {}'.format('Press','Category'))
    
    exit=1
    
    while(True):
        i=0
        print("<<<<<<< MAIN CATEGORY >>>>>>>>")
        for cat in categories.keys():
            i+=1
            print('{}        {}     '.format(i,cat)) 
        
        flag=0
        flag =int(input('\nPlease selecet the category you want to browse by its number : '))
        if flag <=6 :
                 print("\n\n")
                 if flag  ==1:
                         lnames=list(categories["Shoes"][0].keys())
                         lvalues=list(categories["Shoes"][0].values())
                         while(True):
                                 d=1
                                 
                                 for i , p in categories['Shoes'][0].items():
                                        print('{}            {}    {} L.E'.format(d,i,p))
                                        d+=1
                                 flag =int(input('\nPress >> < 0 > to go back. \nChoose the items u wanna buy buy its number >> it will be added to your card :) '))
                                 if flag >= len(list(categories["Shoes"][0].keys()))+1:
                                        print('\nPlease select a number from the given list :)')
                                        continue
                                 if flag ==0 :
                                        break
                                 userItemsCard.append(lnames[flag-1])
                                 userCashAmount.append(lvalues[flag-1])
                                 print('\nSir u have now {} items in your card. \nYou can remove items later before complete your purchasing'.format(len(userItemsCard)))
                                 
                                 
                 elif flag ==2 :
                         lnames=list(categories["Jeans"][0].keys())
                         lvalues=list(categories["Jeans"][0].values())
                         while(True):
                                 d=1
                                 for i , p in categories['Jeans'][0].items():
                                        print('{}            {}    {} L.E'.format(d,i,p))
                                        d+=1
                                 flag =int(input('\nPress >> < 0 > to go back. \nChoose the items u wanna buy buy its number >> it will be added to your card :) '))
                                 if flag >= len(list(categories["Jeans"][0].keys()))+1:
                                        print('\nPlease select a number from the given list :)')
                                        continue
                                 if flag ==0 :
                                        break
                                 userItemsCard.append(lnames[flag-1])
                                 userCashAmount.append(lvalues[flag-1])
                                 print('\nSir u have now {} items in your card. \nYou can remove items later before complete your purchasing'.format(len(userItemsCard)))                                
                                 
                 elif flag ==3 :
                         lnames=list(categories["Shirts"][0].keys())
                         lvalues=list(categories["Shirts"][0].values())
                         while(True):
                                 d=1
                                 for i,p  in categories['Shirts'][0].items():
                                        print('{}            {}    {} L.E'.format(d,i,p))
                                        d+=1
                                 flag =int(input('\nPress >> < 0 > to go back. \nChoose the items u wanna buy buy its number >> it will be added to your card :) '))
                                 if flag >= len(list(categories["Shirts"][0].keys()))+1:
                                        print('\nPlease select a number from the given list :)')
                                        continue
                                 if flag ==0 :
                                        break
                                 userItemsCard.append(lnames[flag-1])
                                 userCashAmount.append(lvalues[flag-1])
                                 print('\nSir u have now {} items in your card. \nYou can remove items later before complete your purchasing'.format(len(userItemsCard)))
                                 
                 elif flag ==4 :
                         lnames=list(categories["T-shirts"][0].keys())
                         lvalues=list(categories["T-shirts"][0].values())
                         while(True):
                                 d=1
                                 for i,p in categories['T-shirts'][0].items():
                                        print('{}            {}     {} L.E'.format(d,i,p))
                                        d+=1
                                 flag =int(input('\nPress >> < 0 > to go back. \nChoose the items u wanna buy buy its number >> it will be added to your card :) '))
                                 if flag >= len(list(categories["T-shirts"][0].keys()))+1:
                                        print('\nPlease select a number from the given list :)')
                                        continue
                                 if flag ==0 :
                                        break
                                 userItemsCard.append(lnames[flag-1])
                                 userCashAmount.append(lvalues[flag-1])
                                 print('\nSir u have now {} items in your card. \nYou can remove items later before complete your purchasing'.format(len(userItemsCard)))
                                 
                 elif flag ==5 :
                         lnames=list(categories["Accessories"][0].keys())
                         lvalues=list(categories["Accessories"][0].values())
                         while(True):
                                 d=1
                                 for i , p  in categories['Accessories'][0].items():
                                        print('{}            {}    {} L.E'.format(d,i,p))
                                        d+=1
                                 flag =int(input('\nPress >> < 0 > to go back. \nChoose the items u wanna buy buy its number >> it will be added to your card :) '))
                                 if flag >= len(list(categories["Accessories"][0].keys()))+1:
                                        print('\nPlease select a number from the given list :)')
                                        continue
                                 if flag ==0 :
                                        break
                                 userItemsCard.append(lnames[flag-1])
                                 userCashAmount.append(lvalues[flag-1])
                                 print('\nSir u have now {} items in your card. \nYou can remove items later before complete your purchasing'.format(len(userItemsCard)))
                                          
        else:
                 print('\nPlease select using numbers ')
                 continue
        exit=int(input("\nIf you want to complete purchasing and pay press <0>\nIf you want to continue shopping press <1>"))
        if exit==0:
            Card()
            break

    


# # Card Function
# 
# 

# In[ ]:


def Card():
    print("\n{} Thanks for choosing our stor <3\nThis is your card of items so far".format(currentUser))
    itemid=1
    print("\n{}    {}    {}".format("ID","Price","Item name"))
    d=0
    s=1
    while(True):
        if d >= len(userItemsCard):
            break
        print("\n{}    {}    {}".format(s,userCashAmount[d-1],userItemsCard[d-1]))
        d+=1
        s+=1
    for i in range(0,len(userCashAmount)):
                userCashAmount[i]=int(userCashAmount[i])
    print("\nYour Total pill is = {}".format(sum(userCashAmount)))
    
    flag=input("\nDo you want to remove items from your card ? <yes/no> ")
    if re.search(r'[yY]|[eE][sS]\s',flag):
        while(itemid):
            itemid=int(input("\nPlease Enter the id of item you want to remove or < 0 > : to complete the payment :) "))
            if (itemid !=0) & (itemid<=len(userItemsCard)):
                del userItemsCard[itemid-1]
                del userCashAmount[itemid-1]
                print("\nYour Total pill is = {}".format(sum(userCashAmount)))
            else:
                print("\nPlease Select item by its id :)")
            for i in range(0,len(userCashAmount)):
                userCashAmount[i]=int(userCashAmount[i])
            print("\nYour Total pill is = {}".format(sum(userCashAmount)))
            print("\nPress <0> to complete your purchasing sir : ")
            Card()

    else:
        for i in range(0,len(userCashAmount)):
                userCashAmount[i]=int(userCashAmount[i])
        print("\nYour Total pill is = {}".format(sum(userCashAmount)))
        print("\nWe Were happy of your visit {}".format(currentUser))
        if usersCountry[currentUser] =="Egypt":
            print("Estimated delivering time less than 4 days :)")
        else:
            print("Estimated delivering time is 7 days :) ")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




