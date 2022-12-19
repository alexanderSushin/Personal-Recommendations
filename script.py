from numpy import *
interesting_ids = [1535, 22319, 32281, 30276, 19815, 28977, 20583, 20899, 14741, 16498, 32182, 23273, 28851, 9253, 5114, 1575, 437, 1, 11061]
f = open("rating.csv", 'r')
users = 73517
mat = full((users, len(interesting_ids)), -1, dtype=int)
f.readline()
for line in f:
    to = list(line.split(','))
    for i in range(len(to)):
        to[i] = int(to[i])
    print(to[0])
    for i in range(len(interesting_ids)):
        if to[1] == interesting_ids[i]:
            mat[to[0]][i] = to[2]
outfile = "mat.npy"
save(outfile, mat)
