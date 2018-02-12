import re
import glob
import numpy as np

out = np.zeros((60, 900))

import pdb;pdb.set_trace()
for f in glob.glob('*[0-9][0-9].txt'):
    m = re.search('[0-9][0-9](?=\.txt)', f)
    try:
        i = int(m.group(0))
        with open(f, 'r') as fh:
            data = np.loadtxt(fh)

    
        out[i-1] = data[:900]

    except ValueError:
        print 'No number found in ' + f
    
    

np.savetxt('Malsburg_change.csv', out, delimiter=",")
