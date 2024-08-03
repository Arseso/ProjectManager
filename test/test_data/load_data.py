import pandas as pd
import os

# splits = {'train': 'data/train-00000-of-00001-b1700331af6d3576.parquet', 'test': 'data/test-00000-of-00001-460abe60f17dbc1c.parquet'}
# df = pd.read_parquet("hf://datasets/ShashiVish/cover-letter-dataset/" + splits["train"])

# splits = {'train': 'data/train-00000-of-00001-68b7166f0e075b40.parquet', 'test': 'data/test-00000-of-00001-52dd46fdb3d0ea34.parquet'}
# df = pd.read_parquet("hf://datasets/kwanyick/cover-letter-dataset-prompt-response/" + splits["train"])

# df = pd.read_parquet("hf://datasets/jenrajaseharan/job_and_cover_letter_dataset/data/train-00000-of-00001-2f471bb1728d9d9c.parquet")

# splits = {'train': 'data/train-00000-of-00001.parquet', 'test': 'data/test-00000-of-00001.parquet'}
# df = pd.read_parquet("hf://datasets/dhruvvaidh/cover-letter-dataset-llama2/" + splits["train"])

# df.to_csv("test_data.csv")



# data = pd.read_csv('test_data.csv')

os.chdir("../../src/data/texts")

# for text in data["Output"]:
#     existing_files = [int(x.split(".")[0]) for x in os.listdir() if x.endswith(".txt")]
#     max_file_number = max(existing_files) + 1 if existing_files else 1

#     new_filename = f"{max_file_number}.txt"

#     with open(new_filename, "w") as f:
#         f.writelines(["To; google_recruitment@google.com\n",
#                       "Subject: Application for Project Manager Position at Google\n"
#                       ])
#         f.write(text)




df = pd.DataFrame(columns=['file', 'text'])

files, texts = [], []

for file in os.listdir():
    files.append(file)
    with open(file, 'r') as f:
        texts.append(f.readlines())

df['file'] , df['text'] = files, texts       
