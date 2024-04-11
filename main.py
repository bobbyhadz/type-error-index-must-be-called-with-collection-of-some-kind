# Index(...) must be called with a collection of some kind

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    columns=['A', 'B', 'C']
)

#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
print(df)