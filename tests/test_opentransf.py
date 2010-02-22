import pymorph
import numpy as np
def test_opentransf():
    f = np.array([
            [0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,1,0,1,1,1,0,0],
            [0,0,1,1,1,1,0,0],
            [1,1,0,0,0,0,0,0]], bool)
    ot = pymorph.opentransf( f, 'city-block')
    for y in xrange(ot.shape[0]):
        for x in xrange(ot.shape[1]):
            r = ot[y,x]
            t = f.copy()
            for k in xrange(1, r+1):
                assert t[y,x]
                t = pymorph.open(f, pymorph.sedisk(k, 2, 'city-block'))
            assert not t[y,x]

