# src/hashing/sha_stats.py
import hashlib
import random
import time
from collections import Counter
import argparse

try:
    import matplotlib.pyplot as plt
    _HAS_MPL = True
except Exception:
    _HAS_MPL = False

try:
    from scipy.stats import binom
    _HAS_SCIPY = True
except Exception:
    _HAS_SCIPY = False

def compute_bit_counts(num_inputs: int):
    bit_counts = []
    start_time = time.time()
    for _ in range(num_inputs):
        random_input = str(random.randint(0, 1 << 30)).encode()
        hash_value = hashlib.sha256(random_input).digest()
        bit_count = sum(bin(byte).count('1') for byte in hash_value)
        bit_counts.append(bit_count)
    elapsed_time = time.time() - start_time
    return bit_counts, elapsed_time

def run(num_inputs: int = 10000, plot: bool = False):
    print(f"Running SHA-256 statistics with {num_inputs} inputs (this may take a moment)...")
    bit_counts, elapsed_time = compute_bit_counts(num_inputs)

    hashes_per_second = num_inputs / elapsed_time if elapsed_time > 0 else float('inf')

    birthday_attack_time_years = (2 ** 128) / hashes_per_second / (3600 * 24 * 365)
    brute_force_attack_time_years = (2 ** 256) / hashes_per_second / (3600 * 24 * 365)

    print("""
Performance Metrics:
Elapsed Time: {elapsed_time:.3f} seconds
Number of Hashes Computed: {num_inputs}
Hashes per Second: {hashes_per_second:.3f}
Time for Birthday Attack: {birthday_attack_time_years:.2e} years
Time for Brute-Force Attack: {brute_force_attack_time_years:.2e} years
""".format(elapsed_time=elapsed_time, num_inputs=num_inputs, hashes_per_second=hashes_per_second, birthday_attack_time_years=birthday_attack_time_years, brute_force_attack_time_years=brute_force_attack_time_years))

    histogram = Counter(bit_counts)

    print("Histogram of 1-bit counts:")
    for bit_count, frequency in sorted(histogram.items()):
        print(f"Bit Count: {bit_count}, Frequency: {frequency}")

    if plot:
        if not _HAS_MPL:
            print("matplotlib is not installed — cannot plot. Install matplotlib to enable plotting.")
        else:
            plt.bar(histogram.keys(), histogram.values(), edgecolor='black')
            plt.xlabel("Bit Count")
            plt.ylabel("Frequency")
            plt.title("Distribution of 1-Bit Counts in SHA-256 Outputs")
            plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
            plt.show()

    if _HAS_SCIPY:
        total_bits = 256
        probability_of_one = 0.5
        probability_128 = binom.pmf(128, total_bits, probability_of_one)
        probability_100 = binom.pmf(100, total_bits, probability_of_one)
        print(f"nThe probability of exactly 128 bits being 1: {probability_128}n")
        print(f"The probability of exactly 100 bits being 1: {probability_100}n")
    else:
        print("\nscipy not installed — skipping binomial PMF calculations (install scipy if you want those).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SHA-256 statistics demo")
    parser.add_argument("--num", type=int, default=10000, help="Number of random inputs to hash (default 10000)")
    parser.add_argument("--plot", action="store_true", help="Show histogram plot (requires matplotlib)")
    args = parser.parse_args()
    run(num_inputs=args.num, plot=args.plot)

