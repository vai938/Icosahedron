import random
import numpy as np
import pandas as pd


def pick_random_sample(arr, sample_size):
    return random.sample(arr, sample_size)


def compute_mean_and_std_dev(arr):
    return (np.mean(arr), np.std(arr))


def verify_central_limit_theorem(arr):
    sample_size = 100
    number_of_experiments = 10000
    means = []

    for i in range(number_of_experiments):
        k = pick_random_sample(arr, sample_size)
        sample_mean = np.mean(k)
        means.append(sample_mean)

    final_mean, final_std_dev = compute_mean_and_std_dev(means)
    population_mean, population_std_dev = compute_mean_and_std_dev(arr)

    print(f"population_mean :: {population_mean}")
    print(f"population_std_dev :: {population_std_dev}")
    print(f"mean_of_sample_means :: {final_mean}")
    print(f"std_dev_of_sample_means :: {final_std_dev}")


def read_data_from_csv_as_array(file_path):
    return pd.read_csv(file_path).to_numpy().tolist()


if __name__ == "__main__":
    arr = read_data_from_csv_as_array("2d_1000000.csv")
    verify_central_limit_theorem(arr)
