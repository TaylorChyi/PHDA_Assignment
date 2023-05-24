import pandas as pd
import matplotlib.pyplot as plt

from data_utils import save

# 加载Excel文件
def excel_reader(filename):
    df1 = pd.read_excel(filename, sheet_name='TwoSteps_sequential', usecols='B:G', skiprows=range(10), nrows=1000)
    df2 = pd.read_excel(filename, sheet_name='TwoSteps_sequential', usecols='J:O', skiprows=range(10), nrows=1000)
    df = pd.concat([df1, df2], axis=1)
    print(df.head())
    print(df.columns)
    return df

def visualize_data(data: pd.DataFrame):
    # Convert columns to numeric, replace 'Undefined' with NaN and drop rows with NaN values
    for column in ['Estimated queue length (patients)', 'Estimated waiting time (hours)', 'Utilisation']:
        data[column] = pd.to_numeric(data[column], errors='coerce')
    data = data.dropna()

    # Sort data by 'Arrival rate (patients/hour)'
    data = data.sort_values(by='Arrival rate (patients/hour)')

    # Plot Arrival rate (patients/hour) vs Estimated waiting time (hours)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Arrival rate (patients/hour)'], data['Estimated waiting time (hours)'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Estimated waiting time (hours)')
    plt.title('Arrival rate vs Estimated waiting time')
    plt.grid()
    save(None, fig, "Arrival rate vs Estimated waiting time")

    # Plot Arrival rate (patients/hour) vs Utilisation
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Arrival rate (patients/hour)'], data['Utilisation'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Utilisation')
    plt.title('Arrival rate vs Utilisation')
    plt.grid()
    save(None, fig, "Arrival rate vs Utilisation")

    # Plot Arrival rate (patients/hour) vs Estimated queue length (patients)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Arrival rate (patients/hour)'], data['Estimated queue length (patients)'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Estimated queue length (patients)')
    plt.title('Arrival rate vs Estimated queue length')
    plt.grid()
    save(None, fig, "Arrival rate vs Estimated queue length")

    # Dropping unwanted columns and rounding off to 2 decimal places
    data = data.drop(columns=['Average service time (hours)', 'Capacity'])
    data = data.round(2)
    save(data, None, "arrival_rate")


def main():
    # Assuming excel_reader function is defined to read the data
    # data = excel_reader('resource/original_output.xlsx')
    data = excel_reader('resource/option_2_output.xlsx')
    
    visualize_data(data)
    
if __name__ == '__main__':
    main()
