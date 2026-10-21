import pandas as pd

data = {
    'Name': ['a','b','c','e'],
    'Marks': ['10','20','30','40']
}
df = pd.DataFrame(data)
df.to_csv('abc.csv', index=False)