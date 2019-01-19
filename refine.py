wc = 0
f = open('text8', 'r')
for line in f.readlines():
    for word in line.split(' '):
        print word
