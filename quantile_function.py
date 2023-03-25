def quant(df, q):
    from math import floor, ceil
    df.sort_values(inplace=True)
    n = len(df)
    index = (n - 1) * q
    if int(index) != index:
        fraction = index - int(index)
        i = df[floor(index)]
        j = df[ceil(index)]
        return i + (j - i) * fraction
    return df[index]


import pandas as pd
a = pd.Series([34, 12, 45, 32, 40])

print(quant(a, q=0.25))
print(a.quantile(0.25))

