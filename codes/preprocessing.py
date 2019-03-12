import pandas as pd

data = pd.read_csv("dataset.min.csv")

labels = ['username', 'Age', 'Gender']

# Replacing URLs
data = data.replace('http\S+|www.\S+', '~', regex=True)

# Replacing mentions
data = data.replace('@\S+', '@', regex=True)

# Removing tweets shorter than 5 characters
data = data.replace('^.{,5}$', '', regex=True)

print(data.head(5))
