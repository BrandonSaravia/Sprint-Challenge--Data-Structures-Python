class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) == self.capacity:
      self.storage[self.current] = item
      self.current += 1
      if self.current == self.capacity:
        self.current = 0
    elif self.storage[0] == None:
      self.storage[0] = item
    else:
      self.storage.append(item)

  def get(self):
    newArr = [r for r in self.storage if r != None]
    return newArr