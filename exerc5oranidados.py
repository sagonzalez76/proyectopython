animales=["gato","perro"]
animalesvacio=[]
for i in animales:
    for j in i:
        animalesvacio.extend(j)
print(animalesvacio)