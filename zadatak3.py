#%%
#1
n=int(input("Unesi broj"))
tot=0
while(n>0):
    dig=n%10
    print(dig)
    tot=tot+dig
    n=n//10

print("Suma znamenki je:",tot)
# %%
#2
password="random"

while True:
    unos=input("Unesite lozinku")
    if password ==unos:
        print("Upisali ste tocnu lozinku")
    else:
        print("Lozinka je netocna")
    break
# %%
#3
import random

num = random.randint(1,10)
guess = None

while guess != num:
    guess = input("Pogodi broj ")
    guess = int(guess)

    if guess == num:
        print("Cestitam pobijedio si")
        break
    else:
        print("Pokusaj ponovno")
    if guess==0:
        break
# %%
#6
num = 123456
print(str(num)[::-1])
# %%
#12
i=0
while i<=10:
    print("asdas")
# %%
#11
number=int(input("Unesi broj"))
count =1
print("tablica za broj",number)
while count<=10:
    number = number*1
    print(number,'x',count,'=',number*count)
    count+=1

# %%
#8
while True:
    number=int(input("Unesite broj"))
    if(number==0):
        break
    if number >=1 and number<=99:
        print(number) 
    # %%
#9
#%%
list=[]

while len(list) <10:
    number=int(input("Unesi cijeli broj"))
    list.append(number)

print(list)
print(sum(list)/ len(list))
print([num //2 for num in list])

# %%
#10a
count = 1
max = 4
while count <= max:
    print("*" * count)
    count +=1


#%%
#10b
k=5
for i in range(0,5,2):
    for j in range(1,(k-2)+1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
#%%


# %%
#13
broj=int(input("Unesite broj"))

if broj==0:
    print("Result:1")
elif broj==1:
    print("Result:1")
total = 1
count = 1
while count<= broj:
    total *= count
    count +=1
print("Result",total)
# %%
#15
list=[]
while True:
    number=int(input("Unesite broj"))
    if(number==0):
        break
    else:
        list.append(number)
print(sum(list))


# %%
#14
num1=int(input("Unesi prvi broj"))
num2=int(input("Unesi drugi broj"))
broj=1
count=1

while count <=num1 or count <= num2:
    if num1% count ==0 and num2 % count ==0:
        broj= count
    count +=1

print("Najveci zajednicki djelitelj je",broj)
# %%
