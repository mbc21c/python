f = open('out.txt',  'w')
print(1, 2, 3, 4, 5, file = f)
f.close()
f = open('out.txt').read()

print(f)