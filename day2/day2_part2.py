data = open('input')
abc = list('ABC')
xyz = list('XYZ')

totalscore = 0
for line in data:
    v = line.strip('\n').split(' ')
    myindex = xyz.index(v[1])
    elfindex = abc.index(v[0])

    # Win=6, Draw=3, Loss=0
    totalscore += myindex*3
    
    # Selected value
    if myindex == 0:
        res = (elfindex-1) % 3
    elif myindex == 1:
        res = elfindex
    elif myindex == 2:
        res = (elfindex+1) % 3
    totalscore += res+1

print(totalscore)
