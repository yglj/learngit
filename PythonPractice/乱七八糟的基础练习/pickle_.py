# encoding = utf-8
import pickle
list = ['a','b','c']
with open("b.txt","wb") as f:
    pickle.dump(list,f)
del list
with open("b.txt","rb") as f:
    new_list = pickle.load(f)
    print(new_list)