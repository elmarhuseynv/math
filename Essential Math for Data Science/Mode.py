from collections import defaultdict

sample = [0,1, 8, 7, 1, 5, 6, 7]

def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_counts = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_counts]
    return modes
print(mode(sample))
