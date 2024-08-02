import pandas as pd
import os
os.chdir("./src/data")
df = pd.read_csv("./responses_as_num.csv")

texts_dir = "./texts/"
texts = []
for filename in df.filename:
    with open(texts_dir+filename, mode='r') as file:
        texts.append("".join(file.readlines()))
df["text"] = texts

df.to_csv("./responces_modified.csv")
        
