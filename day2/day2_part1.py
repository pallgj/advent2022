data = open('input')
abc = list('ABC')
xyz = list('XYZ')

totalscore = 0
for line in data:
    v = line.strip('\n').split(' ')
    myindex = xyz.index(v[1])
    elfindex = abc.index(v[0])

    # Rock=X=1, Paper=Y=2, Scissors=Z=3
    totalscore += myindex+1

    # Win=6, Draw=3, Loss=0
    # Set draw as default (=3). Win: mod=1, loss: mod=2
    mod = (myindex-elfindex) % 3
    wld = 3
    if mod == 1:
        wld = 6
    elif mod == 2:
        wld = 0
    totalscore += wld
print(totalscore)
