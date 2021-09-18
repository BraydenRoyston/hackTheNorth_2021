import pandas as pd
file_name = "bad_songs.xlsx"
sheet = "Sheet1"
cols=[1,5]
df = pd.read_excel(io=file_name, sheet_name=sheet, engine='openpyxl', usecols=cols)
out = df.to_json(orient="records")

with open('bad.json', 'w') as f:
    f.write(out)

