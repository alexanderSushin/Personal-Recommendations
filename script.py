import numpy as np
import pandas as pd
interesting_ids = [1535, 22319, 32281, 30276, 19815, 28977, 20583, 20899, 14741, 16498, 32182, 23273, 28851, 9253, 5114, 1575, 437, 1, 11061]
f = pd.read_csv('rating.csv')
users = 59381
mat = np.full((users, len(interesting_ids)), -1, dtype=int)
arr = []
cnt = 0
data = f[f["anime_id"].isin(interesting_ids)]
for index, row in data.iterrows():
    if len(arr) == 0 or arr[-1] != row["user_id"]:
        arr.append(row["user_id"])
    id = len(arr) - 1
    for i in range(len(interesting_ids)):
        if interesting_ids[i] == row["anime_id"]:
            mat[id][i] = row["rating"]
            break

outfile = "mat.npy"
np.save(outfile, mat)
