def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a dictionary to keep track
    weight_dicto = {}

    # Iterate through the list of weights, adding each to dictionary
    # key: weight, value: limit - weight
    for weight in weights:
        if weight not in weight_dicto:
            weight_dicto[weight] = limit-weight

    # Iterate through the dictionary and determine if the limit-weight
    # of the current weight are in our original list of weights
    # If so, then find the index of both and return
    for weight in weight_dicto.items():
        print(weight)
        # If there are only two items in our list, reverse the list and grab first index on the last, then grab first index of the first
        if len(weights) == 2:
            result = [len(weights) - 1 - weights[::-1].index(weights[1]), weights.index(weight[1])]

            return result
        if weight[1] in weights:
            return [weights.index(weight[1]), weights.index(weight_dicto[weight[1]])]

    return None
