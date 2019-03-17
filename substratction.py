l = ["Claudia", "Jeff", "Gilbert", "Garreth"]
m = ("Claudia", "Jeff", "Gilbert", "Garreth")

type(l)
type(m)
print(m)
print(len(m))
print(l)
print(len(l))
l.append("Jenelle")
l.insert(0, "Jeanice")

def add(n):
  for i in l:
    l.append(n)
print(add)

add("Joe")
print(add)
print("Garreth")
