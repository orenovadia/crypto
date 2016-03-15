PT1 = "dawn"
PT2 = "dusk"
#458e7e53f36
C1 = [0xe7,0xe5,0x3f,0x36]
p1b = [ord(i) for i in PT1]
p2b = [ord(i) for i in PT2]
key = [x^y for x,y in zip(p1b,C1)]
print key
print '09e1c5f70a65ac519458'+''.join(    map(str , map(hex, [x^y for x,y in zip(key,p2b)]) )  )
