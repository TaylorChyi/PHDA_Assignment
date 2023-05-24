import os
import pandas as pd
from typing import Any
import config
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_preprocess_data():
    data = pd.read_csv(config.FILE_PATH)
    data['Arrival_Time'] = pd.to_datetime(data['Arrival_Time'])
    data['Time_Seen'] = pd.to_datetime(data['Time_Seen'])
    data['Departure_Time'] = pd.to_datetime(data['Departure_Time'])
    data['Departure_Hour'] = data['Departure_Time'].dt.hour
    
    # Convert 'Arrival_Time' and 'Time_Seen' to timedelta by using only the time part
    data['Arrival_Time'] = pd.to_timedelta(data['Arrival_Time'].dt.strftime('%H:%M:%S'))
    data['Arrival_Hour'] = np.floor(data['Arrival_Time'].dt.total_seconds() / 3600)
    data['Time_Seen'] = pd.to_timedelta(data['Time_Seen'].dt.strftime('%H:%M:%S'))
    
    # Convert 'Arrival_Date' to datetime
    data['Arrival_Date'] = pd.to_datetime(data['Arrival_Date'])
    
    # Combine 'Arrival_Date' and 'Arrival_Time' to a single datetime column
    data['Arrival_Datetime'] = data['Arrival_Date'] + data['Arrival_Time']
    
    # If 'Time_Seen' is earlier than 'Arrival_Time', assume it's on the next day
    next_day_mask = data['Time_Seen'] < data['Arrival_Time']
    data.loc[next_day_mask, 'Arrival_Date'] = data.loc[next_day_mask, 'Arrival_Date'] + pd.Timedelta(days=1)
    
    # Combine 'Arrival_Date' and 'Time_Seen' to a single datetime column
    data['Time_Seen_Datetime'] = data['Arrival_Date'] + data['Time_Seen']
    
    # Calculate the waiting time in minutes
    data['Waiting_Time_Minutes'] = (data['Time_Seen_Datetime'] - data['Arrival_Datetime']).dt.total_seconds() / 60

    
    return data

def plotting(x_values, y_values, x_labels, y_labels, title, rotation=0):
    plt.figure(figsize=(10, 6))
    plot = sns.barplot(x=x_values, y=y_values, color='skyblue')
    plt.xlabel(x_labels)
    plt.ylabel(y_labels)
    plt.title(title)
    plt.grid(True)
    plot.set_xticklabels(plot.get_xticklabels(), rotation=rotation, horizontalalignment='right')
    plt.tight_layout()
    return plot
    
def save(result, plot, file_name):
    if config.TEXT_STATE and result is not None:
        save_analysis_result(result, file_name)
    if config.PLOT_STATE and plot is not None:
        save_plot(plot, file_name)
    if config.PRINT_STATE:
        print_analysis_result(result, file_name)
        

def print_analysis_result(result, file_name):
    print(file_name)
    print(result)
    print("================================")
    
def save_analysis_result(result, file_name):
    result_file_path = os.path.join(config.TEXT_OUTPUT_DIR, file_name + config.TEXT_SUFFIX)
    if isinstance(result, pd.DataFrame):
        # If the result is a DataFrame, use the to_csv method for saving
        result.to_csv(result_file_path, index=False, header=False)
    else:
        # If the result is not a DataFrame (e.g., a simple string), save it as before
        with open(result_file_path, 'w') as f:
            f.write(str(result))

def save_plot(plot, file_name):
    plot.figure.savefig(os.path.join(config.PLOT_OUTPUT_DIR, file_name + config.PLOT_SUFFIX))
