import os
import pandas as pd

def load_df_with_names(path, anomaly=""):
    
    if anomaly not in ["valve1", "valve2", "other", "all", ]:
        raise ValueError("Unexpected anomaly type")
        
    if anomaly == "all":
        anomaly = ""

    all_files=[]
    file_names=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                all_files.append(os.path.join(root, file))
                
                
    list_of_df=[]          
    for file in all_files:
        if 'anomaly-free' not in file and anomaly in file and ".ipynb_checkpoints" not in file:
            list_of_df.append(pd.read_csv(file, sep=';', index_col='datetime', parse_dates=True))
            file_names.append(file)
            
    anomaly_free_df = pd.read_csv([file for file in all_files if 'anomaly-free' in file][0], 
                                  sep=';', index_col='datetime', parse_dates=True)
    return list_of_df, anomaly_free_df, file_names


def load_df_by_names(path, anomalies):
    res = {}
    
    for anomaly in anomalies:
        list_of_df, _, file_names = load_df_with_names(path, anomaly)
        for df, name in zip(list_of_df, file_names):
            res[name] = df
    return res
