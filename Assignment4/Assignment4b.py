import hashlib
import random
import matplotlib.pyplot as plt #May have to use "pip install matplotlib" for histogram implementation
from collections import Counter
import time  # For timing performance
from scipy.stats import binom # May have to use "pip install scipy" for binomial probability

def main():
    # Number of hashes to compute
    num_inputs = 100000  # Adjust this for reasonable runtime
    bit_counts = []

    # Start timing
    start_time = time.time()

    # Generate random inputs, compute hashes, and count 1-bits
    for _ in range(num_inputs):
        #Generate a random input
        random_input = str(random.randint(0, 1 << 30)).encode()
        
        #Compute SHA-256 hash
        hash_value = hashlib.sha256(random_input).digest()
        
        # Count the number of 1 bits in the hash
        bit_count = sum(bin(byte).count('1') for byte in hash_value)
        bit_counts.append(bit_count)

    #End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    

    # Performance metrics
    hashes_per_second = num_inputs / elapsed_time

    # Estimate time for birthday attack (2^128 hashes)
    birthday_attack_time_years = (2 ** 128) / hashes_per_second / (3600 * 24 * 365)

    # Estimate time for brute-force attack (2^256 hashes)
    brute_force_attack_time_years = (2 ** 256) / hashes_per_second / (3600 * 24 * 365)

    # Print timing and performance results
    print("\nPerformance Metrics:")
    print(f"Elapsed Time: {elapsed_time:.3f} seconds")
    print(f"Number of Hashes Computed: {num_inputs}")
    print(f"Hashes per Second: {hashes_per_second:.3f}")
    print(f"Time for Birthday Attack: {birthday_attack_time_years:.2e} years")
    print(f"Time for Brute-Force Attack: {brute_force_attack_time_years:.2e} years\n")
    
    # Create a histogram of bit counts
    
    histogram = Counter(bit_counts)

    # Print the histogram data
    
    print("Histogram of 1-bit counts:")
    for bit_count, frequency in sorted(histogram.items()):
        print(f"Bit Count: {bit_count}, Frequency: {frequency}")
    
    
    # Plot the histogram using matplotlib
    
    plt.bar(histogram.keys(), histogram.values(), color='blue', edgecolor='black')
    plt.xlabel("Bit Count")
    plt.ylabel("Frequency")
    plt.title("Distribution of 1-Bit Counts in SHA-256 Outputs")
    plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.show()
    

    # Histogram must be closed before attempting to run again.

    

# Define the total number of bits and the probability of a bit being 1
total_bits = 256
probability_of_one = 0.5

# Calculate the probability of 128 bits being set to 1
probability_128 = binom.pmf(128, total_bits, probability_of_one)

# Calculate the probability of  100 bits being set to 1
probability_100 = binom.pmf(100, total_bits, probability_of_one)

# Display the results in scientific notation
print(f"\nThe probability of exactly 128 bits being 1: {probability_128}\n")
print(f"The probability of exactly 100 bits being 1: {probability_100}\n")


if __name__ == "__main__":
    main()


