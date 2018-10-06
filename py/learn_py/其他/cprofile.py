import cProfile

##a = 'abc'
##b = '123'
def one():
     a = 'abc'*1000000
     b = '123'*1000000
     result = a+b

def two():
     a = 'abc'*1000000
     b = '123'*1000000
     result = '%s%s'%(a,b)

def three():
     a = 'abc'*1000000
     b = '123'*1000000
     result = '{}{}'.format(a,b)

def four():
     a = 'abc'*1000000
     b = '123'*1000000
     result = '{0}{1}'.format(a,b)


if __name__  == '__main__':
     cProfile.run('one()')
     cProfile.run('two()')
     cProfile.run('three()')
     cProfile.run('four()')
