class Pilha(object):

  def __init__(self, len):
    self.topo = -1
    self.len = len
    self.vetor = []

  def push(self, valor):
    if self.topo != self.len:
      self.topo += 1
      self.vetor.append(valor)

  def pop(self):
    while self.isEmpty() != True:
      aux = self.topo
      self.topo -= 1
      print(self.vetor[aux])

  def isFull(self):
    return self.topo == len(self.vetor) - 1

  def isEmpty(self):
    return self.topo == -1

  def palindromo(self):
    return self.vetor == self.vetor[::-1]