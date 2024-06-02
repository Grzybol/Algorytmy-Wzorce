import timeit
import os

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            results.append(i)
    return results

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []
    bad_char = {}

    # Fill the bad character dictionary
    for i in range(m):
        bad_char[pattern[i]] = i

    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            results.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1) if shift + m < n else 1)
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))

    return results

def compare_search_algorithms(pattern):
    print("Starting comparison of search algorithms...\n")

    # Ensure the text file is in the correct path
    file_path = 'text.txt'
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist in the current directory.")
        return

    # Read text from file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Time naive algorithm
    start_time = timeit.default_timer()
    naive_results = naive_search(text, pattern)
    naive_time = timeit.default_timer() - start_time
    print(f"Naive search results: {naive_results}")
    print(f"Naive search time: {naive_time:.6f} seconds\n")

    # Time Boyer-Moore algorithm
    start_time = timeit.default_timer()
    boyer_moore_results = boyer_moore_search(text, pattern)
    boyer_moore_time = timeit.default_timer() - start_time
    print(f"Boyer-Moore search results: {boyer_moore_results}")
    print(f"Boyer-Moore search time: {boyer_moore_time:.6f} seconds\n")

    # Compare times
    print("Summary:")
    if naive_time < boyer_moore_time:
        print(f"Naive search was faster by {boyer_moore_time - naive_time:.6f} seconds")
    else:
        print(f"Boyer-Moore search was faster by {naive_time - boyer_moore_time:.6f} seconds")

# Sample pattern
pattern = "celestial"

# Run comparison
if __name__ == "__main__":
    compare_search_algorithms(pattern)
    input("Press Enter to exit...")