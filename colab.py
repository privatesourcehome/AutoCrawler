import pandas as pd
url = "C:/1234/x_train_response.csv"
df = pd.read_csv(url, names=['F1','F2','F3','F4','F5','D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','R1'])
df.head()