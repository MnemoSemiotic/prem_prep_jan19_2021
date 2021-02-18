from random import choice


def get_bit():
    return choice([0,1])


def generate_binary(n=8):
    return [get_bit() for bit in range(n)]


def get_float(n=8):
    bin_list = generate_binary(n)

    flt_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        flt_accum += bit * 0.5**idx

    return flt_accum, bin_list

# print(get_float(n=8))


