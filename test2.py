def scalar_product(v1, v2):
    """
    compute the product of two vectors .
    AI-generated by Ponicode.
    """
    assert len(v1) == len(v2)
    scalar_product = sum(v1[i]*v2[i] for i in range(len(v1)))
    return scalar_product

def is_palindrome(s):
    """
    checks if s is a palindrome .
    AI-generated by Ponicode.
    """
    return s[::-1] == s
