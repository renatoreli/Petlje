#%%
#1
for i in range(3,9):
    print(i)
#%%
#2
i=20
while i>4:
    print(i)
    i -= 1

# %%
#3
for i in range(0,5):
    print(i*2)
# %%
#4
for i in range(0,8):
    print(i**2)

# %%
#5
for i in range(0,5):
    if i%2==0:
        print(i)
# %%
#6
for i in range(0,5):
    if i%2==1:
        print(i)

# %%
#7
for i in range(1,7):
    if i%3==0:
        print(i)
# %%
#8
def numbers(n):
    for i in range(3, n+1):
        print(i)
numbers(20)
# %%
#9
count=1
n=20
a=2
lista=[]
while count <=n :
    if count % a != 0:
        lista.append(count)
    count +=1
print(sum(lista))
# %%
#10
lista =[0,1,2,3,4]
lista1=[]
for broj in lista:
    if broj%3 !=0:
        print(broj)
        lista1.append(broj)
print(sum(lista1)/len(lista1))
# %%
