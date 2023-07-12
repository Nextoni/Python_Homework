def nan_expand(times):
    result = ""

    for time in range(times):
        if time < times:
            result += "Not a "
    result += "NaN"

    return result

print(nan_expand(3))