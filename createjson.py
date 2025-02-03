import os, json

directory = {"_base":"https://raw.githubusercontent.com/gamesbyangelina/strudel/main/"};

for subdir, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".mp3"):
            # print(subdir[2:])
            # print(file)
            cat = subdir[2:]
            if not cat in directory:
                directory[cat] = []
            directory[cat].append(subdir[2:]+"/"+file)
            #hello i am lazy
            directory[cat] = sorted(directory[cat])

with open("strudel.json", "w") as f:
    f.write(json.dumps(directory))

exit()
