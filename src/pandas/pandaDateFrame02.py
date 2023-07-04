import pandas as pd

dfmi = pd.DataFrame([list('abcd'),
            list('efgh'),
            list('ijkl'),
            list('mnop')],
            columns=pd.MultiIndex.from_product([['one', 'two'],
                                                ['first', 'second']]))

print(dfmi)

print(dfmi['one']['second'])
print(dfmi.loc[:,('one','second')])