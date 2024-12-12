import os, json

directory = {"_base":"https://raw.githubusercontent.com/gamesbyangelina/strudel/main/"};

for file in os.listdir("."):
    if file.endswith(".mp3"):
        cat = file.split('-')[0]
        if not cat in directory:
            directory[cat] = []
        directory[cat].append(file)
        #hello i am lazy
        directory[cat] = sorted(directory[cat])
        
with open("strudel.json", "w") as f:
    f.write(json.dumps(directory))