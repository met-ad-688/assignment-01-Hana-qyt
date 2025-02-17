import pandas as pd
import os
files = ["question_tags.csv", "questions.csv"]  
count = 0

for file in files:
    if not os.path.exists(file):
        print(f"⚠️ File not found: {file}, skipping...")
        continue
    print(f"📂 Processing {file} ...", flush=True)
    try:
        chunk_size = 100000
        for chunk in pd.read_csv(file, encoding='utf-8', usecols=["Tag"], on_bad_lines='skip', chunksize=chunk_size):
            count += chunk["Tag"].astype(str).str.contains("GitHub", case=False, na=False).sum()

    except Exception as e:
        print(f"⚠️ Error reading {file}: {e}", flush=True)
        continue   
with open("_output/github_count.txt", "w") as f:
    f.write(str(count))
print(f"✅ Total lines containing 'GitHub': {count}", flush=True)
