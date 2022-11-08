import numpy as np
import matplotlib.pyplot as plt

# Exercise 1.2

# function to generate 101 samples of vector with n features
def generate_samples(n):
    samples = np.zeros((n, 101))
    for i in range(0, 101):
        samples[:, i] = np.random.uniform(0, 1, n)
    return samples


# function to calculate min and max euclidean distance
def max_and_min_dist(samples):
    random_sample_num = np.random.randint(0, 102)
    random_sample = samples[:, random_sample_num]

    distances = []
    for i in range(0, 101):
        if i != random_sample_num:
            other_sample = samples[:, i]
            distance = np.linalg.norm(random_sample - other_sample)
            distances.append(distance)

    d_max = max(distances)
    d_min = min(distances)
    return d_min, d_max


# function to compute r
def compute_r(d_min, d_max):
    r = (d_max - d_min)/d_min
    return r

# find r when n = 10
n = 10
samples = generate_samples(n)
d_min, d_max = max_and_min_dist(samples)
r = compute_r(d_min, d_max)
print("\nExercise 1.2")
print("      r: ", r)


# Exercise 1.3

# find r for the different values of n
n_list = [1, 10, 100, 10**3, 10**4, 10**5]
r_list = []
for n in n_list:
    samples = generate_samples(n)
    d_min, d_max = max_and_min_dist(samples)
    r = compute_r(d_min, d_max)
    r_list.append(r)

n_log_list = np.log10(n_list)

print("\nExercise 1.3")
print("    n = ", n_list)
print("    r = ", r_list)

# graph r as a function of n
plt.plot(n_log_list, r_list)
plt.title('r as a function of n')
plt.xlabel('log n')
plt.ylabel('r')
plt.show()










