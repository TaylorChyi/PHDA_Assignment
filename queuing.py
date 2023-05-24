from math import factorial
import scipy.stats as stats

def calculate_queue_metrics(lmbda, mu, s):
    rho = lmbda / mu / s

    # Make sure the system is stable (i.e., the arrival rate is less than the service rate)
    if rho < 1:
        # Calculate the probability of 0 patients in the system
        sum_probs = sum([(s * rho) ** n / factorial(n) for n in range(s)])
        prob_0 = 1 / (sum_probs + (s * rho) ** s / (factorial(s) * (1 - rho)))

        # Calculate the average queue length
        Lq = (rho ** s * lmbda * mu * prob_0) / (factorial(s - 1) * (s * mu - lmbda) ** 2)

        # Calculate the average wait time
        Wq = Lq / lmbda
    else:
        print("The system is not stable. The arrival rate must be less than the service rate.")
        Lq = float('inf')
        Wq = float('inf')

    return Lq, Wq, rho

print(calculate_queue_metrics(10, 4,4))