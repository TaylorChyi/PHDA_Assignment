import pandas as pd
import numpy as np
from data_utils import *
   
def analyze_problem_category_count(data):
    problem_counts = data['problem'].value_counts()
    plot = plotting(problem_counts.index, 
                problem_counts.values, 
                'Problem Category (minutes)', 
                'Number of problem category', 
                'Distribution of problem category',
                45)
    
    save(problem_counts, plot, 'problem_category_distribution')
    return problem_counts

def analyze_waiting_time_count_per_hour(data: pd.DataFrame):
    # Describe the waiting time
    waiting_time_description = data['Waiting_Time_Minutes'].describe()

    # Count the number of data points with waiting time equal to 0
    waiting_time_zero_count = (data['Waiting_Time_Minutes'] == 0).sum()
    
    # Group waiting times into 10-minute bins
    bins = np.arange(0, data['Waiting_Time_Minutes'].max() + 10, 10)
    waiting_time_bins = pd.cut(data['Waiting_Time_Minutes'], bins).value_counts().sort_index()

    # Plotting
    plot = plotting(waiting_time_bins.index.astype(str), 
                    waiting_time_bins.values, 
                    'Waiting Time (minutes)', 
                    'Frequency', 
                    'Distribution of Waiting Time',
                    45)

    # Save or print the results
    save(waiting_time_bins, plot, 'waiting_time_count')
    save(waiting_time_zero_count, None, 'waiting_time_zero_count')
    save(waiting_time_description, None, 'waiting_time_description')
    
    return waiting_time_description

def analyze_service_time_count_per_hour(data: pd.DataFrame):
    # Convert the service time to minutes for easier interpretation
    data['Service_Time_Minutes'] = data['Service_Time_secs'] / 60
    
    # Describe the service time
    service_time_description = data['Service_Time_Minutes'].describe()

    # Group service times into 10-minute bins
    bins = np.arange(0, data['Service_Time_Minutes'].max() + 10, 10)
    service_time_bins = pd.cut(data['Service_Time_Minutes'], bins).value_counts().sort_index()

    # Plotting
    plot = plotting(service_time_bins.index.astype(str), 
                    service_time_bins.values, 
                    'Service Time (minutes)', 
                    'Frequency', 
                    'Distribution of Service Time',
                    45)

    # Save or print the results
    save(service_time_description, plot, 'service_time_description')
    
    return service_time_description

def analyze_arrival_time_count_per_hour(data: pd.DataFrame):
    # Count the number of arrivals in each hour
    arrival_time_distribution = data['Arrival_Hour'].value_counts().sort_index()
    
    # Plotting
    plot = plotting(arrival_time_distribution.index, 
                    arrival_time_distribution.values, 
                    'Hour of the Day', 
                    'Number of Arrivals', 
                    'Distribution of Arrival Times')
    
    # Save or print the results
    save(arrival_time_distribution, plot, 'arrival_time_distribution')
    
    return arrival_time_distribution

def analyze_arrival_rate_per_hour(data: pd.DataFrame):
    # Count the number of arrivals in each hour
    arrival_time_distribution = (data['Arrival_Hour'].value_counts()/365).sort_index()
    
    # Plotting
    plot = plotting(arrival_time_distribution.index, 
                    arrival_time_distribution.values, 
                    'Hour of the Day', 
                    'Arrival Rate', 
                    'Distribution of Arrival Rate')
    
    # Save or print the results
    save(arrival_time_distribution, plot, 'arrival_rate_distribution')
    
    return arrival_time_distribution

def analyze_waiting_time_stats_per_problem(data: pd.DataFrame):
    # Calculate descriptive statistics for waiting time for each problem category
    waiting_time_stats_per_problem = data.groupby('problem')['Waiting_Time_Minutes'].describe()

    # Save the result
    save(waiting_time_stats_per_problem, None, 'waiting_time_stats_per_problem')

    return waiting_time_stats_per_problem

def analyze_departure_time(data: pd.DataFrame):
    # Count the number of departures in each hour
    departure_time_distribution = data['Departure_Hour'].value_counts().sort_index()
    
    # Plotting
    plot = plotting(departure_time_distribution.index, 
                    departure_time_distribution.values, 
                    'Hour of the Day', 
                    'Number of Departures', 
                    'Distribution of Departure Times')
    
    # Save or print the results
    save(departure_time_distribution, plot, 'departure_time_distribution')
    
    return departure_time_distribution

def analyze_service_time_per_problem(data: pd.DataFrame):
    # Group the data by problem and calculate average service time
    service_time_per_problem = data.groupby('problem')['Service_Time_secs'].mean().sort_values(ascending=False)

    # Convert the service time to minutes for easier interpretation
    service_time_per_problem = service_time_per_problem / 60
    
    # Plotting
    plot = plotting(service_time_per_problem.index, 
                    service_time_per_problem.values, 
                    'Problem', 
                    'Average Service Time (minutes)', 
                    'Average Service Time per Problem',
                    45)
    
    # Save or print the results
    save(service_time_per_problem, plot, 'service_time_per_problem')
    
    return service_time_per_problem

def analyze_avg_service_time_per_hour(data: pd.DataFrame):
    # Group the data by arrival hour and calculate average service time
    service_time_per_hour = data.groupby('Arrival_Hour')['Service_Time_secs'].mean().sort_index()

    # Convert the service time to minutes for easier interpretation
    service_time_per_hour = service_time_per_hour / 60
    
    # Plotting
    plot = plotting(service_time_per_hour.index, 
                    service_time_per_hour.values, 
                    'Hour of the Day', 
                    'Average Service Time (minutes)', 
                    'Average Service Time per Hour of the Day')
    
    # Save or print the results
    save(service_time_per_hour, plot, 'service_time_per_hour')
    
    return service_time_per_hour

def analyze_waiting_time_per_problem(data: pd.DataFrame):
    # Group the data by problem and calculate average waiting time
    waiting_time_per_problem = data.groupby('problem')['Waiting_Time_Minutes'].mean().sort_values(ascending=False)

    # Convert the waiting time to minutes for easier interpretation
    waiting_time_per_problem = waiting_time_per_problem / 60
    
    # Plotting
    plot = plotting(waiting_time_per_problem.index, 
                    waiting_time_per_problem.values, 
                    'Problem', 
                    'Average Waiting Time (minutes)', 
                    'Average Waiting Time per Problem',
                    45)
    
    # Save or print the results
    save(waiting_time_per_problem, plot, 'waiting_time_per_problem')
    
    return waiting_time_per_problem

def analyze_zero_waiting_time_by_symptom(data: pd.DataFrame):
    # Initialize a new DataFrame to store the results
    results = []   
     
    # Group by 'Symptom'
    grouped = data.groupby('problem')
    
    for name, group in grouped:
        # Count the total number of data points in the group
        total_count = group.shape[0]
        
        # Count the number of data points with waiting time equal to 0 in the group
        zero_count = (group['Waiting_Time_Minutes'] == 0).sum()
        
        # Calculate the percentage
        zero_percentage = zero_count / total_count * 100
        
        # Append the results to the list
        results.append({'Symptom': name, 'Zero_Count': zero_count, 'Total_Count': total_count, 'Zero_Percentage': zero_percentage})
    
    # Convert the list to a DataFrame
    result = pd.DataFrame(results)
    # Save the result
    save(result, None, 'zero_waiting_time_by_symptom')
    
    
    # Plotting
    plot = plotting(result['Symptom'], 
                    result['Zero_Count'],
                    'Symptom',
                    'Count of Zero Waiting Time',
                    'Count of Zero Waiting Time by Symptom',
                    45)
    save(None, plot, 'zero_count_by_symptom')

    plot = plotting(result['Symptom'], 
                result['Zero_Percentage'],
                'Symptom',
                'Percentage of Zero Waiting Time',
                'Percentage of Zero Waiting Time by Symptom',
                45)
    


    save(None, plot, 'zero_percentage_by_symptom')


    # Return the result DataFrame
    return result

def analyze_efficiency(data: pd.DataFrame):
    # Define the list of problems handled by emergency nurses
    nurse_problems = ["muscular or tendon injuries", "sprains", 
                      "bruises and grazes", "cuts", "fractures and dislocations"]

    # Identify the data points handled by doctors and nurses
    data['Handled_By'] = data['problem'].apply(lambda x: 'Nurse' if x in nurse_problems else 'Doctor')

    # Exclude 'other' and 'left without being seen'
    filtered_data = data[~data['problem'].isin(['other', 'left without being seen'])]

    # Calculate the average service time for doctors and nurses
    avg_service_time = filtered_data.groupby('Handled_By')['Service_Time_secs'].mean()

    # Calculate the efficiency (hour per case)
    efficiency = avg_service_time / 3600 # There are 3600 seconds in an hour

    # Save the results
    save(efficiency, None, 'efficiency')

    return efficiency

def analyze_transferred_cases(data: pd.DataFrame):
    # Create a new column to indicate whether each case was transferred
    data['Is_Transferred'] = data['note'].apply(lambda x: 'transferred after seen' in x.lower())

    # Calculate the total number of cases and the number of transferred cases for each problem
    problem_counts = data['problem'].value_counts()
    transferred_counts = data[data['Is_Transferred']]['problem'].value_counts()

    # Calculate the proportion of transferred cases for each problem
    transferred_proportions = transferred_counts / problem_counts

    # Add total number of cases and overall transfer proportion to the results
    total_case = pd.Series({'Total': problem_counts.sum()}, name='Problem')
    transferred_counts = pd.concat([transferred_counts, total_case])

    total_transferred = transferred_counts.sum()
    total_transfer_proportion = pd.Series({'Total': (total_transferred - problem_counts.sum()) / problem_counts.sum()}, name='Problem')
    transferred_proportions = pd.concat([transferred_proportions, total_transfer_proportion])

    # Plotting
    plot1 = plotting(transferred_counts.index, transferred_counts.values, 'Problem', 'Transferred Count', 'Count of Transferred Cases per Problem')
    plot2 = plotting(transferred_proportions.index, transferred_proportions.values, 'Problem', 'Transferred Proportion', 'Proportion of Transferred Cases per Problem', 45)
    
    # Save the results
    save(transferred_counts, plot1, 'transferred_counts')
    save(transferred_proportions, plot2, 'transferred_proportions')

    return transferred_counts, transferred_proportions

def analyze_problem_counts(data: pd.DataFrame):
    # Exclude 'other' and 'left without being seen'
    filtered_data = data[~data['problem'].isin(['other', 'left without being seen'])].copy()

    # Define the problems handled by emergency practice nurses
    nurse_problems = ["muscular or tendon injuries", "sprains", "bruises and grazes", "cuts", "fractures and dislocations"]

    # Assign each case to a role based on the problem
    filtered_data.loc[:,'Role'] = filtered_data['problem'].apply(lambda x: 'Nurse' if x in nurse_problems else 'Doctor')

    # Calculate the total number of cases for each role
    role_counts = filtered_data['Role'].value_counts()

    # Calculate the number of "other" and "left without being seen" cases
    other_cases = data[data['problem'] == 'other'].shape[0]
    left_cases = data[data['problem'] == 'left without being seen'].shape[0]

    # Add "other" and "left without being seen" cases to the results
    other_left_total_counts = pd.Series({'Other': other_cases, 'Left': left_cases, 'Total': data.shape[0]})
    role_counts = pd.concat([role_counts, other_left_total_counts])

    # Plotting
    plot = plotting(role_counts.index, role_counts.values, 'Role', 'Count', 'Count of Cases per Role',45)

    # Save the results
    save(role_counts, plot, 'role_counts')

    return role_counts

def lwbs_analysis(df):
    # Filter rows where 'note' contains the text 'left without being seen'
    df['LWBS'] = np.where(df['note'].str.contains('left without being seen'), 1, 0)

    # Group by the 'hour' column and sum the 'LWBS' column
    LWBS_hourly = df.groupby('Arrival_Hour')['LWBS'].sum()

    # To get the ratio, divide the sum by the total count for each hour
    LWBS_ratio_hourly = LWBS_hourly / df.groupby('Arrival_Hour')['LWBS'].count()

    plot = plotting(LWBS_ratio_hourly.index, 
                LWBS_ratio_hourly.values, 
                'Hour', 
                'Number of Left Without Being seen', 
                'LWBS_ratio_hourly')
    # Output the result
    save(LWBS_ratio_hourly, plot, 'LWBS_ratio_hourly')    
    
def analyze_avg_wait_time_per_hour(data: pd.DataFrame):
    # Group the data by arrival hour and calculate average service time 
    waiting_time_per_hour = data.groupby('Arrival_Hour')['Waiting_Time_Minutes'].mean().sort_index()
    
    # Plotting
    plot = plotting(waiting_time_per_hour.index, 
                    waiting_time_per_hour.values, 
                    'Hour of the Day', 
                    'Average Waiting Time (minutes)', 
                    'Average Waiting Time per Hour of the Day')
    
    # Save or print the results
    save(waiting_time_per_hour, plot, 'waiting_time_per_hour')
    
    return waiting_time_per_hour

def calculate_hourly_cases(df):
    # Calculate the hour of arrival
    df['Arrival_Hour'] = df['Arrival_Datetime'].dt.hour

    # Group by problem and arrival hour and count the number of cases
    problem_hourly_cases = df.groupby(['problem', 'Arrival_Hour']).size().reset_index(name='Cases')

    # Save the result to a CSV file
    problem_hourly_cases.to_csv('problem_hourly_cases.csv', index=False)

    # Create a bar plot for each problem
    problems = problem_hourly_cases['problem'].unique()
    for problem in problems:
        sub_df = problem_hourly_cases[problem_hourly_cases['problem'] == problem]
        plt.bar(sub_df['Arrival_Hour'], sub_df['Cases'])
        plt.xlabel('Hour of Arrival')
        plt.ylabel('Number of Cases')
        plt.title(f'Number of Cases per Hour for {problem}')
        plt.savefig(f'{problem}_cases_per_hour.png')
        plt.clf()  # Clear the current figure for the next plot
    
def calculate_hourly_cases_by_professional(df):
    # Define the problems handled by the emergency nurse practitioner
    nurse_problems = ["muscular or tendon injuries", "sprains", "bruises and grazes", "cuts", "fractures and dislocations"]
    
    # Create a new column 'Professional' based on the problem
    df['Professional'] = df['problem'].apply(lambda x: 'Emergency Nurse Practitioner' if x in nurse_problems else 'General Practitioner')
    
    # Calculate the hour of arrival
    df['Arrival_Hour'] = df['Arrival_Datetime'].dt.hour
    
    # Group by professional and arrival hour, and count the number of cases
    professional_hourly_cases = df[df['problem'] != 'other'].groupby(['Professional', 'Arrival_Hour']).size().reset_index(name='Cases')
    
    # Save the result to a CSV file
    professional_hourly_cases.to_csv('professional_hourly_cases.csv', index=False)
    
    # Create a bar plot for each professional
    professionals = professional_hourly_cases['Professional'].unique()
    for professional in professionals:
        sub_df = professional_hourly_cases[professional_hourly_cases['Professional'] == professional]
        plt.bar(sub_df['Arrival_Hour'], sub_df['Cases'])
        plt.xlabel('Hour of Arrival')
        plt.ylabel('Number of Cases')
        plt.title(f'Number of Cases per Hour handled by {professional}')
        plt.savefig(f'{professional}_cases_per_hour.png')
        plt.clf()  # Clear the current figure for the next plot

def calculate_hourly_cases_difference(df):
    # Define the problems handled by the emergency nurse practitioner
    nurse_problems = ["muscular or tendon injuries", "sprains", "bruises and grazes", "cuts", "fractures and dislocations"]
    
    # Create a new column 'Professional' based on the problem
    df['Professional'] = df['problem'].apply(lambda x: 'Emergency Nurse Practitioner' if x in nurse_problems else 'General Practitioner')
    
    # Calculate the hour of arrival
    df['Arrival_Hour'] = df['Arrival_Datetime'].dt.hour
    
    # Group by professional and arrival hour, and count the number of cases
    professional_hourly_cases = df[df['problem'] != 'other'].groupby(['Professional', 'Arrival_Hour']).size().reset_index(name='Cases')

    # Pivot the DataFrame to have professionals as columns
    pivot_df = professional_hourly_cases.pivot(index='Arrival_Hour', columns='Professional', values='Cases').reset_index()

    # Calculate the difference in number of cases between General Practitioner and Emergency Nurse Practitioner
    pivot_df['Difference'] = (pivot_df['Emergency Nurse Practitioner'] - pivot_df['General Practitioner']) / 365

    # Save the result to a CSV file
    pivot_df.to_csv('professional_hourly_cases_difference.csv', index=False)
    
    # Plot the difference
    plot = plotting(pivot_df['Arrival_Hour'], pivot_df['Difference'], 'Hour of Arrival', 'Difference in Number of Cases', 'Difference between Emergency Nurse and GP')
    save_plot(plot, 'cases_difference_per_hour.png')
    
def main():
    data = load_and_preprocess_data()
    calculate_hourly_cases_difference(data)
    
if __name__ == '__main__':
    main()
