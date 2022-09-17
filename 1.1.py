
modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']
indices = []
characters = []
for i,j in enumerate(modern_family):
    indices.append(i)
    characters.append(j)
print(indices)
print()
print(characters)
print()
l = len(characters)

for x in range(l):
    characters[x] = characters[x].lower().replace("_","-")

print(characters)
print()

temp = list(map(lambda x:len(x) , characters))
print(temp)
print()

for i,j in zip(zip(indices,temp),range(l)):
    indices[j] = sum(i)
print(indices)
print()

indices.sort(reverse=True)
print(indices)
print()
Phew_finally = {}

for x in range(l):
    Phew_finally[indices[x]] = characters[x]
print(Phew_finally)

    