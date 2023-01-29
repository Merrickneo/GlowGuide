from emoji_remover import emoji_remover

import pandas as pd

df = pd.read_csv("Data/black_honey.csv")
df = df[df.iloc[:, 0] != "[deleted]"]

# Mine doesn't have emojis surprisingly so i just removed the deleted rows

df.to_csv("Data/black_honey_clean.csv", index=False)
