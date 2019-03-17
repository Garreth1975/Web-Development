petnames = []
while True:
     print("the names of the pet name " + str(len(petnames) +1))
     name = input()
     if name == "":
          break
     petnames = petnames + [name]
print("The animals are")
for name in petnames:
    print(" " + name)
