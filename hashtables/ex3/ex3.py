def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Get the length of inner arrays
    arrs_len = len(arrays)

    # Create a cache
    cache = {}

    # Iterate throught the arrays
    for array in arrays:
        # Iterate through the internal array
        for num in array:
            if num not in cache:
                cache[num] = 1
            # If the number is already in the cache
            # increment it by one
            else:
                cache[num] += 1

    # create a list of results
    # this will be the final return
    result = []

    # iterate through the cache, append ints that have equal
    # occurances to that on the inner arrays
    for pair in cache.items():
        if pair[1] == arrs_len:
            result.append(pair[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
