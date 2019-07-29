# conda activate mydashenv
import numpy as np
import pandas as pd
'''
mat = np.arange(0,50).reshape(5,10)

df = pd.DataFrame(data=mat)
print(df)
'''


mat = np.arange(0,10).reshape(5,2)

df = pd.DataFrame(data=mat, columns=['A','B'])
print(df)