class StrIntMap:
  def __init__(self, capacity=8):
    self.capacity = capacity
    self.tab = [[] for _ in range(capacity)]
    self.cnt = 0

  def get_index(self, key):
    return hash(key) % self.capacity
  
  def put(self, key, value):
    index = self.get_index(key)
    bucket = self.tab[index]

    for p in bucket:
      if p[0] == key:
        p[1] = value
        return
      
    bucket.append([key, value])
    self.cnt += 1

  def get(self, key):
    index = self.get_index(key)
    bucket = self.tab[index]

    for p in bucket:
      if p[0] == key:
        return p[1]
    return None
  
  def remove(self, key):
    index = self.get_index(key)
    bucket = self.tab[index]

    for i,p in enumerate(bucket):
      if p[0] == key:
        bucket.pop(i)
        self.cnt -= 1
        return

  def contains(self, key):
    if self.get(key) is None:
      return False
    return True
  
  def size(self):
    return self.cnt
  
  def keys(self):
    res = []
    for bucket in self.tab:
      for p in bucket:
        res.append(p[0])
    return res
  
  def rehash(self):
    old_table = self.tab

    self.capacity = self.capacity * 2
    self.tab = [[] for _ in range(self.capacity)]
    self.cnt = 0

    for bucket in old_table:
      for pair in bucket:
        key = pair[0]
        value = pair[1]
        self.put(key, value) 