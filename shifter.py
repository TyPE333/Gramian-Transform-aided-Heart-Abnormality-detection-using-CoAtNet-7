var_names = [["gasf_train", "gasf_train_label"], ["gasf_test", "gasf_test_label"], ["gasf_val", "gasf_val_label"], 
            ["gadf_train", "gadf_train_label"], ["gadf_test", "gadf_test_label"], ["gadf_val", "gadf_val_label"]]
cur_dir = "/common/VIT/sem6/data_viz_theory/data_viz_project/Image_data/"
import os
import pandas as pd
import shutil
# os.mkdir("gsdf_data")
for csv in var_names:
    name_df = pd.read_csv(f"{cur_dir}/split_csv/{csv[0]}.csv")
    label_df = pd.read_csv(f"{cur_dir}/split_csv/{csv[1]}.csv")
    name_list = name_df['file_name'].tolist()
    label_list = label_df['encoding'].tolist()
    gasf_or_gadf = csv[0].split("_")[0].upper()
    next_dir = cur_dir + gasf_or_gadf + "/"
    split = csv[0].split("_")[1]
    root_dir = f"{cur_dir}{gasf_or_gadf.lower()}_split/"
    new_dir = f"{root_dir}{split}/"
    if os.path.exists(root_dir) == False:
        os.mkdir(root_dir)
    os.mkdir(new_dir)
    normal_dir = new_dir + "normal/"
    abnormal_dir = new_dir + "abnormal/"
    os.mkdir(normal_dir)
    os.mkdir(abnormal_dir)
    for i in range(len(name_list)):
        if label_list[i] == 0:
            src = next_dir + "Abnormal/" + name_list[i]
            dst = abnormal_dir
        else:
            src = next_dir + "Normal/" + name_list[i]
            dst = normal_dir
        shutil.copy(src, dst)