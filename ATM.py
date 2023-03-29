##with open("Hesaplar.txt",'w',encoding = 'utf-8') as f:
   ##f.write("my first file\n")
   ##f.write("This file\n\n")
   ##f.write("contains three lines\n")
   ##print('yazdım')
   
##f = open("Hesaplar.txt",'r',encoding = 'utf-8')
##print(f.read()) 
##f.close()
##print('kapattım') 

def logintration():
    print('write your name')
    a=input()
    print('write your own password')
    b=input()
    f = open("Hesaplar.txt",'r',encoding = 'utf-8')
    Fare=f.read()
    print(f.read()) 
    f.close()
    sonuc=Fare.find(a+':'+b+'\n')
    if sonuc==-1:
      print('error!')
    else:
      print('succesfully logginned')
      bakiye = open(a+".txt",'r',encoding = 'utf-8')
      mugofare=bakiye.read()
      mugofare=int(mugofare)
      print('What action would you like to take? \n 1-withdraw money \n 2-to deposit money \n 3-view your own budget')
      k=input()
      if int(k)==1:
        print('how much money you want to withdraw?')
        l=input()
        l=int(l)
        if l>mugofare:
          print('error!\n if you want turn back to main menu type 0')
          j=input()
          j=int(j)
          if j==0:
            turnback(a)
        else:
          newbudget=(int(mugofare-l)) 
          newbudget=str(newbudget)
          print(str(l)+'  process completed.your new budget:'+newbudget+' \n if you want turn back to main menu type 0')
          with open(a+".txt",'w',encoding = 'utf-8') as bakiye:
            bakiye.write(newbudget)
            j=input()
            j=int(j)
            if j==0:
              turnback(a)
          
      if int(k)==2:
        print('how much money you want to deposit?')
        m=input()
        m=int(m)
        newbudget=(mugofare+m)
        newbudget=str(newbudget)
        print('process completed.your new budget:'+newbudget+' \n if you want turn back to main menu type 0')
        with open(a+".txt",'w',encoding = 'utf-8') as bakiye:
            bakiye.write(newbudget)
            j=input()
            j=int(j)
            if j==0:
              turnback(a)
       
      if int(k)==3:
         budget=str(mugofare)
         print('your budget ='+budget+' \n if you want turn back to main menu type 0' )
         j=input()
         j=int(j)
         if j==0:
           turnback(a)
def turnback(a):
      bakiye = open(a+".txt",'r',encoding = 'utf-8')
      mugofare=bakiye.read()
      mugofare=int(mugofare)
      print('What action would you like to take? \n 1-withdraw money \n 2-to deposit money \n 3-view your own budget')
      k=input()
      if int(k)==1:
        print('how much money you want to withdraw?')
        l=input()
        l=int(l)
        if l>mugofare:
          print('error!')
        else:
          newbudget=(int(mugofare-l)) 
          newbudget=str(newbudget)
          print(str(l)+'  process completed.your new budget:'+newbudget)
          with open(a+".txt",'w',encoding = 'utf-8') as bakiye:
            bakiye.write(newbudget)
          
      if int(k)==2:
        print('how much money you want to deposit?')
        m=input()
        m=int(m)
        newbudget=(mugofare+m)
        newbudget=str(newbudget)
        print('process completed.your new budget:'+newbudget)
        with open(a+".txt",'w',encoding = 'utf-8') as bakiye:
            bakiye.write(newbudget)
       
      if int(k)==3:
         budget=str(mugofare)
         print('your budget ='+budget)
  


def registration():
  print ('write your name')
  x=input()
  print('write your password')
  y=input()
  print('write your password again')
  z=input()
  print('type your first budget')
  s=input()
  if z!=y:
     print('error!') 
     quit()
  with open("Hesaplar.txt",'a',encoding = 'utf-8') as f:
     f.write(x+':'+y+'\n')
  with open(x+".txt",'a',encoding = 'utf-8') as f:
     f.write(s)  
     print('you registered succesfully \n if you want turn back to main menu type 0')
     j=input()
     j=int(j)
     if j==0:
       turnback(x)



print('login or register')

x = input()
if x=='1':
  print('logining')
  logintration()
  




else:
  print('registering')
  registration()
 

 

   

