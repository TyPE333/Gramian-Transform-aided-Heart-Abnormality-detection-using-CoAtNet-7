import os
import re
import pandas as pd
dir = "/common/VIT/sem6/data_viz_theory/data_viz_project/2016_dataset/training/hea_combined/"
labels = []
files_with_errors = [[], [438, 441, 451, 452, 456, 462, 464, 465, 468, 470, 472, 482], [454], [339, 351], [88, 187], [], []]
x = sorted(os.listdir(dir))
for i in range(len(x)):
    with open(os.path.join(dir, x[i])) as f:
        text = f.read()
        list = re.findall(r"# (\w+)", text)
        labels.append(list[0])
print(len(labels))
labels_chunks = [labels[x:x+500] for x in range(0, len(labels), 500)]
for i in range(len(labels_chunks)):
    if len(files_with_errors[i]) > 0:
        for index in files_with_errors[i]:
            # labels_chunks[i].pop(index-1)
            labels_chunks[i][index-1] = "ERROR"
i = 0
for chunk in labels_chunks:
    a = pd.DataFrame(chunk)
    a.to_csv(".".join(["complete_labels_"+str(i), "csv"]), header = False, index = None)
    i+=1