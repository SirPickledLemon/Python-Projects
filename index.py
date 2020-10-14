print("Hello World")
#convert elevator floors
inp = input('Europe floor: ')
usf = int(inp) + 1
print('US floor' , usf)

#if statements
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')

#try/except to move past a traceback error (if this blows up, it moves onto different code rather than stopping)
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First' , istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second' , istr)

#define function (def)
def thing():
    print('Hello')
    print('Fun')
thing()
print('Wow')
thing()