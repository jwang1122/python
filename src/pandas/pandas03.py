"""
Check for equality
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[1,2,np.nan], 'b':[1,2,np.nan]})

print(df)

print(df.a == df.b)
print(np.nan==np.nan)
print(df.a.equals(df.b))
print(type(np.nan))

l1 = [1,2,3]
l2 = [1,2,3]
print(l1==l2)
print(l1)
print(l2)

dfNew = df.copy()
print(dfNew.equals(df)) # True

df = pd.DataFrame({'c':[1,2,3],'d':[1.,2.,3.], 'e':[1.0, 2.0, 3.000005]})
print(df)

print(df.c.equals(df.d)) # False
pd.testing.assert_series_equal(df.c, df.d, check_names=False, check_dtype=False)
pd.testing.assert_series_equal(df.d, df.e, check_names=False, check_exact=False)

dfNew = df.copy()
pd.testing.assert_frame_equal(df, dfNew)