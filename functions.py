def add(a, b):
    return a + b

def scalar_product(v1, v2):
    assert len(v1) == len(v2)
    scalar_product = sum(v1[i]*v2[i] for i in range(len(v1)))
    return scalar_product