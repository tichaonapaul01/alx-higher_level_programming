def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')
            result += (a ** b) / i
        except ValueError:
            result = b + a
            break

    return result
