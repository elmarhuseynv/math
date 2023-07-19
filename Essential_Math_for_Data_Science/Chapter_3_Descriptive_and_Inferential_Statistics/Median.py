sample = [1, 2, 3, 4, 5]

def median(values):
    ordered = sorted(values)

    n = len(values)
    mid = int(n/2) - 1 if n%2==0 else int(n%2)
    if n%2 == 0:
        return(ordered[mid] + ordered[mid+1])
    else: 
        return ordered[mid]
    
print(median(sample))