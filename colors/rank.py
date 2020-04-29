import itertools
import cv2
import numpy as np
import json

def rank(imgpath: str, outpath=r'./color_rank.json', top=10):

    img = cv2.imread(imgpath)
    resh = img.reshape((-1, 3))
    arr = np.unique(resh, axis=0, return_counts=True)

    d = [(c, u) for u, c in zip(*arr) if 2 < c]
    d.sort(key=lambda k:k[0], reverse=True)

    gp = itertools.groupby(d,key=lambda k:k[0])
    uk = []
    vs = []
    for k, v in gp:
        uk.append(k)
        vs.append(list(v))

    item = [{'rank': i+1, 'count': str(uk[i]), 'color': list(map(lambda c: r'rgb({}, {}, {})'.format(c[1][2], c[1][1], c[1][0]), vs[i]))} for i in range(0, min(top, len(uk)))]
    _writeFile(json.dumps(item))


def _writeFile(txt:str, outpath:str):
    with open(outpath, 'w') as f:
        f.write(txt)

