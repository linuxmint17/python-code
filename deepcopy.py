#!/usr/bin/env python3
import copy
person=['name',['saving',100.00]]
hubby=person
wifey = copy.deepcopy(person)
print([id(x) for x  in person, hubby, wifey])
hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)
print([id(x) for x in hubby])
print([id(x) for x  in  wifey])



