

import pandas as pd
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

s = pd.Series([2, 4, 6, 8, 10])
print(s)
print(type(s))

df2 = pd.DataFrame({'X':s, 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
#print(df2)
print('TEST')
print(df2['Y'])
print(type(df2['Y']))
print(df2[['Y']])
print(type(df2[['Y']]))