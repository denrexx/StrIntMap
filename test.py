from main import StrIntMap

m = StrIntMap()

m.put("cat", 10)
m.put("dog", 7)
m.put("mouse", 11)

print(m.get("mouse"))
print(m.get("squirrel"))

print(m.contains("dog"))

m.remove("dog")

print(m.keys())
print(m.size())

m.rehash()

print(m.keys())