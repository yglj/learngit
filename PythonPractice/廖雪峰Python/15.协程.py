

def consumer(): 
     while True:
          p = yield 'ready'
          if p:
               print('consummer...%s'%p)




def product(c):
     c.send(None)
     n = 0
     while n<5:
          n += 1
          print('product...%s'%n)
          msg = c.send(n)
          print('consumer return %s'%msg)

c = consumer()
product(c)
          
