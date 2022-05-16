from pilha import Pilha
esc = input('Qual a sequência? ')

p = Pilha(len(esc))

class Main(object):
  
  def add():
    for i in esc:
      if p.isFull():
        p.push(i)

  def palin():
    if p.palindromo():
      print('É palíndromo')
    else:
      print('Não é palíndromo')
  
  add()
  p.pop()
  palin()