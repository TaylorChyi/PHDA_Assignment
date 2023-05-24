import pandas as pd
import matplotlib.pyplot as plt

from data_utils import save

# 加载Excel文件
def excel_reader(filename):
    df = pd.read_excel(filename, sheet_name=1, usecols='B:G', skiprows=range(1, 10), nrows=1000)
    print(df.head())
    print(df.columns)
    return df

def visualize_data(data: pd.DataFrame):
    # Convert columns to numeric, replace 'Undefined' with NaN and drop rows with NaN values
    for column in ['Unnamed: 5', 'Unnamed: 6']:
        data[column] = pd.to_numeric(data[column], errors='coerce')
    data = data.dropna()

    # Sort data by 'Unnamed: 1'
    data = data.sort_values(by='Unnamed: 1')

    # Plot Arrival rate (patients/hour) vs Estimated waiting time (hours)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Unnamed: 1'], data['Unnamed: 6'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Estimated waiting time (hours)')
    plt.title('Arrival rate vs Estimated waiting time')
    plt.grid()
    # plt.show()
    save(None, fig, "Arrival rate vs Estimated waiting time")

    # Plot Arrival rate (patients/hour) vs Utilisation
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Unnamed: 1'], data['Unnamed: 4'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Utilisation')
    plt.title('Arrival rate vs Utilisation')
    plt.grid()
    # plt.show()
    save(None, fig, "Arrival rate vs Utilisation")

    # Plot Arrival rate (patients/hour) vs Estimated queue length (patients)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Unnamed: 1'], data['Unnamed: 5'])
    plt.xlabel('Arrival rate (patients/hour)')
    plt.ylabel('Estimated queue length (patients)')
    plt.title('Arrival rate vs Estimated queue length')
    plt.grid()
    # plt.show()
    save(None, fig, "Arrival rate vs Estimated queue length")

    data = data.drop(columns=['Unnamed: 2', 'Unnamed: 3'])
    data = data.round(2)
    save(data, None, "arrival_rate")

def main():
    # Assuming excel_reader function is defined to read the data
    # data = excel_reader('resource/original_output.xlsx')
    data = excel_reader('resource/option_1_output.xlsx')
    
    visualize_data(data)
    
if __name__ == '__main__':
    main()
