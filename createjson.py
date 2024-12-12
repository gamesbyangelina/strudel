import os, json

jsonobj = {"_base":"https://raw.githubusercontent.com/gamesbyangelina/strudel/main/"};



for file in os.listdir("."):
    if file.endswith(".mp3"):
        cat = file.split('-')[0]
        if not cat in jsonobj:
            jsonobj[cat] = []
        jsonobj[cat].append(file)
        
with open("strudel.json", "w") as f:
    f.write(json.dumps(jsonobj))