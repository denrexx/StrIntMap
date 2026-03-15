class StrIntMap:
  def __init__(self, capacity=8):
    self.capacity = capacity
    self.tab = [[] for _ in range(capacity)]
    self.cnt = 0

  def get_index(self, key):
    return hash(key) % self.capacity

  def put(self, key, value):
    bucket = self.tab[self.get_index(key)]
    for p in bucket:
      if p[0] == key:
        p[1] = value
        return
    bucket.append([key, value])
    self.cnt += 1

  def get(self, key):
    for k,v in self.tab[self.get_index(key)]:
      if k == key:
        return v
    return None

  def remove(self, key):
    bucket = self.tab[self.get_index(key)]
    for i,(k,v) in enumerate(bucket):
      if k == key:
        bucket.pop(i)
        self.cnt -= 1
        return

  def contains(self, key):
    return self.get(key) is not None

  def size(self):
    return self.cnt

  def keys(self):
    return [k for bucket in self.tab for k,_ in bucket]

  def rehash(self):
    old = self.tab
    self.capacity *= 2
    self.tab = [[] for _ in range(self.capacity)]
    self.cnt = 0
    for bucket in old:
      for k,v in bucket:
        self.put(k,v)
