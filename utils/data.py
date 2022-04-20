import os
import pandas as pd
import numpy as np

def load_df(path, anomaly=''):

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
