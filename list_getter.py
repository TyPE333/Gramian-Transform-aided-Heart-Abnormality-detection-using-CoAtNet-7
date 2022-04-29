import os
dir = "/common/VIT/sem6/data_viz_theory/data_viz_project/2016_dataset/training/training_combined/"
x = sorted(os.listdir(dir))
for i in range(len(x)):
    print(i+1, x[i])