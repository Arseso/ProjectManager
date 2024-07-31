import pandas as pd

# splits = {'train': 'data/train-00000-of-00001-b1700331af6d3576.parquet', 'test': 'data/test-00000-of-00001-460abe60f17dbc1c.parquet'}
# df = pd.read_parquet("hf://datasets/ShashiVish/cover-letter-dataset/" + splits["train"])

# df.to_csv("test_data.csv")

import os

data = pd.read_csv('test_data.csv')

os.chdir("../../src/data/texts")

for text in data["Cover Letter"]:
    existing_files = [int(x.split(".")[0]) for x in os.listdir() if x.endswith(".txt")]
    max_file_number = max(existing_files) + 1 if existing_files else 1

    new_filename = f"{max_file_number}.txt"

    with open(new_filename, "w") as f:
        f.writelines(["To; google_recruitment@google.com\n",
                      "Subject: Application for Project Manager Position at Google\n"
                      ])
        f.write(text)
