from data_analysis import *

def main():
    data = load_and_preprocess_data()
    # analyze_problem_category_count(data)
    
    # analyze_waiting_time_count_per_hour(data)
    
    # analyze_service_time_count_per_hour(data)
    # analyze_arrival_time_count_per_hour(data)
    # analyze_waiting_time_stats_per_problem(data)
    # analyze_departure_time(data)
    # analyze_service_time_per_problem(data)
    # analyze_waiting_time_per_problem(data)
    # analyze_avg_service_time_per_hour(data)
    # analyze_waiting_time_per_problem(data)
    
    # analyze_zero_waiting_time_by_symptom(data)
    
    
    # analyze_efficiency(data)
    # analyze_transferred_cases(data)
    analyze_problem_counts(data)
    
if __name__ == '__main__':
    main()
