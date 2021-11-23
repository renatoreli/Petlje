#%%
#1
gradovi=["Lipik","Pakrac","Zagreb","Osijek","Rijeka"]
gradovi.reverse()
print(gradovi)
gradovi.sort()
print(gradovi)
#%%
#2
gradovi=["Lipik","Pakrac","Zagreb","Osijek","Rijeka"]
print(gradovi[-1])
gradovi.insert(0,"Rijeka")
print(gradovi)
for b in gradovi:
    print(gradovi[1:5])

# %%
#3
gradovi=["Lipik","Pakrac","Zagreb","Osijek","Rijeka"]
for i in gradovi:
    print(i)
# %%
#4
lista =[]
n=int(input("Unesi broj elemenata: "))
for i in range(0,n):
    e=int(input())

    lista.append(e)
print(lista)
# %%
#5
lista=[1,2,3,4,5,-1,-3]
print(max(lista))
print(min(lista))
# %%
#6
lista = ["Ivan","Renato","Božo", "Mario","Roberto"]
longest_name =lista[0]
for name in lista:
    if len(name) > len(longest_name):
        longest_name=name
print(longest_name)

# %%
#7
lista =[]
n=int(input("Unesi broj ocjena: "))
for i in range(0,n):
    e=int(input())

    lista.append(e)
print(sum(lista)/ len(lista))
# %%
#8
names = ["Ivic","Peric","Horvat","Jozinović"]
years = [21,20,54,69]

zipped= zip(names,years)
sort=sorted(zipped)

tuples=zip(*sort)
c = [list(tuple) for tuple in tuples]
print(c)
# %%
#9
lista=[1,2,3,4,5,6,7,8,9]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
# %%
#10

bodovi =[12,33,82,45,67]

bodovi.sort(reverse=True)
print(bodovi[1])

# %%
#11
bodovi = [12,33,82,45,67]
current = 0
best_player = bodovi[0]
for i in range(len(bodovi)):
    current_points= bodovi[i]
    if current_points >best_player:
        best_player = current_points
        current = i
print("Najbolji rezultat je", best_player)
print("Igrao je",current+1,"po redu")
# %%
#12
lista=["a","a","b","c","d","d"]
print(list(set(lista)))

# %%
#13
bodovi = [12,33,82,45,67]
sort=sorted(bodovi)

print("Najbolji rezultat je", sort[0])
print("Najgori rezultat je",sort[-1])

# %%
#14
bodovi=[23,45,43,29 ,50]
sort=sorted(bodovi)
sort.pop()
sort.pop(0)

print(sort)
print(sum(sort))


# %%
#15
lista=[ 2,4,6,8,10]
kvadrat=[lista**2 for lista in lista]
print(kvadrat)

# %%
#16 
list1 = ["Petar", 2, 3, 4, "Pero", "auto", "kuća"]
strings = []
numbers = []
for item in list1:
    if isinstance(item, str):
        strings.append(item)
    else:
        numbers.append(item)
 
print(strings)
print(numbers)
# %%
