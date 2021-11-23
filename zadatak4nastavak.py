#16
#%%
broj=int(input("Unesi broj"))
if broj%3==0:
    print("plava")
elif broj%3==1:
    print("zelena")
elif broj%3==2:
    print("crvena")
else:
    print("zuta")

# %%
#19
operation=input("unesi operaciju")
if operation =="*":
    a=int(input("Unesi prvi broj"))
    b=int(input("Unesi drugi broj"))
    print("Umnozak",a*b)
elif operation =="/":
    a=int(input("Unesi prvi broj"))
    b=int(input("Unesi drugi broj"))
    print("Kolicnik",a/b)
elif operation =="+":
    a=int(input("Unesi prvi broj"))
    b=int(input("Unesi drugi broj"))
    print("Zbroj",a+b)
elif operation =="-":
    a=int(input("Unesi prvi broj"))
    b=int(input("Unesi drugi broj"))
    print("Razlika", a-b)
# %%
#18
a=int(input("Unesi prvu stranicu"))
b=int(input("Unesi drugu stranicu"))
c=int(input("Unesi trecu stranicu"))
print(a,b,c)
if a==b and b==c and a==c:
    print("Trokut je jednakostranican")
elif a!=b and b==c:
    print("Trokut je jednakokracan")
else:
    print("Trokut je raznostranican")
# %%
#17
a=int(input("Unesi broj u intervalu 1-12"))
if a==1:
    print("Sijecanj")
elif a==2:
    print("Veljaca")
elif a==3:
    print("Ožujak")
elif a==4:
    print("Travanj")
elif a==5:
    print("Svibanj")
elif a==6:
    print("Lipanj")
elif a==7:
    print("Srpanj")
elif a==8:
    print("Kolovoz")
elif a==9:
    print("Rujan")
elif a==10:
    print("Listopad")
elif a==11:
    print("Studeni")
elif a==12:
    print("Prosinac")
# %%
#20

a=int(input("Unesi ocjenu 1-5"))
if a ==2 or a==3 or a==4 or a==5:
    print("Prosli ste")
elif a>5:
    print("Nepostojeca ocjena")
else:
    print("Pali ste")

# %%
#21
a=int(input("Unesi broj"))
if a%2==0:
    print("Broj je paran")
else:
    print("Broj je neparan")
# %%
#22
lista =[]
n=int(input("Unesi broj ocjena: "))
for i in range(0,n):
    e=int(input())

    lista.append(e)
print("Prosjek je",sum(lista)/ len(lista))
print(lista)
# %%
