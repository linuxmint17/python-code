#!/usr/bin/env python2.7
'check the name is valid or not'
import string
alphas=string.letters+'_'
nums=string.digits
alphanums=alphas+nums
print 'welcom to the Identifier checker ver1.0'
print 'Testees must be at least 2 chars long.'
myInput=raw_input('Inditifier to to test?\n')

if len(myInput)>1:

  if myInput[0] not in alphas:
    print "invalid :first symbol must be alphabetic"
  else:
    for otherchar in myInput[1:]:
      if otherchar not in alphanums:
        print "invalid:reamining symbols must be alphanumer"
        break
    else:
      print "ok as an identifier"