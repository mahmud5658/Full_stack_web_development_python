def remove_trailing_zeros(S):
    # Check if there's a decimal point in the input
    if '.' in S:
        # Split the input into the whole part and the fractional part
        whole, fraction = S.split('.')
        # Remove trailing zeros from the fractional part
        fraction = fraction.rstrip('0')
        # If the fractional part is now empty, return only the whole part
        if fraction == '':
            return whole
        # Otherwise, return the whole part with the cleaned fractional part
        return f"{whole}.{fraction}"
    else:
        # If there's no decimal point, return the input as it is
        return S

# Input
S = input()
# Output
print(remove_trailing_zeros(S))
