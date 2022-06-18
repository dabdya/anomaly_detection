import os
import pandas as pd
import numpy as np
from IPython.display import display, Markdown, Latex


def load_df(path, anomaly=""):
    
    if anomaly not in ["valve1", "valve2", "other", "all", ]:
        raise ValueError("Unexpected anomaly type")
        
    if anomaly == "all":
        anomaly = ""

    all_files=[]
    for root, dirs, files in os.walk("./data/"):
        for file in files:
            if file.endswith(".csv"):
                 all_files.append(os.path.join(root, file))
            
    list_of_df = [pd.read_csv(file, sep=';', index_col='datetime', parse_dates=True) 
                  for file in all_files if 'anomaly-free' not in file and anomaly in file]

    anomaly_free_df = pd.read_csv([file for file in all_files if 'anomaly-free' in file][0], 
                                  sep=';', index_col='datetime', parse_dates=True)
    return list_of_df, anomaly_free_df

# Generated training sequences for use in the model.
def create_sequences(values, time_steps):
    output = []
    for i in range(len(values) - time_steps + 1):
        output.append(values[i : (i + time_steps)])
    return np.stack(output)


def show_score_table(metrics:dict) -> None:
    columns = list(metrics.keys())
    metrics_arr = np.array(list(metrics.values()))
    metric_names = ["F1", "FAR", "MAR"]
    table = []
    table.append(" | ".join(["metric"] + columns))
    table.append(" | ".join(["---" for _ in range(len(columns) + 1)]))
    for i in range(metrics_arr.shape[-1]):
        row = metrics_arr[:, i]
        table.append(f"{metric_names[i]} |" + " | ".join(map(lambda x: str(round(x, 2)), row)))
    table_str = "\n".join(table)    
    display(Markdown(table_str))

    
def load_df_with_names(path, anomaly=""):
    
    if anomaly not in ["valve1", "valve2", "other", "all", ]:
        raise ValueError("Unexpected anomaly type")
        
    if anomaly == "all":
        anomaly = ""

    all_files=[]
    file_names=[]
    for root, dirs, files in os.walk("./data/"):
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