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

#continue statement jumps to the next iteration of the loop
#break statement ends the loop entirely
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

#for statements
#i just goes through the list until there are no more values to go through
for i in [5, 4, 3, 2, 1]:
    print(i)
print('blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for i in friends:
    print('Happy New Year', i)
print('Done!')

largest_so_far = -1
print('Before', largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
print('After', largest_so_far)