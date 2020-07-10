def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a cache
    cache = {}

    # Size the cache and add the keys, set values to None
    for i in a :
        if i not in cache:
            cache[i] = None

    # Create a final list to be returned
    result = []

    # Iterate through the cache
    # If the key is positive and 
    # has a matching negative(true value)
    # then add the value 
    for true_num in cache.items():
        if true_num[0] > 0 and -true_num[0] in cache:
            result.append(true_num[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
