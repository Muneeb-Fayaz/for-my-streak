import pandas as pd
data={
    'Name':['a','b','c','e'],
    'Marks':['10','20','30','40']
}
data=pd.DataFrame(data)
data.to_csv('abc.csv', index=False)