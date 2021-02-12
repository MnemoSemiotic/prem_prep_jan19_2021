from random import choice, random

def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')




def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1] # list(reversed(bin_list))

# print(dec_to_bin(43, n_bits=8))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
    
    return bins_d

# for dec, bin_ in get_binary(n_bits=8).items():
#     print(f'{dec}: {bin_}')


def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, val in bin_dict.items():
        sum_bits = sum(val)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=12)

# # for the counts
# for k, v in d.items():
#     print(f'{k}: {v}')

# # for the probabilities
# for k, v in d.items():
#     print(f'{k}: {v / sum(d.values())}')


# # prob of getting 4 or less heads in 12 fair coin flips
# (d[0] + d[1] + d[2] + d[3] + d[4]) / sum(d.values()


'''
Binomial through sampling
'''


def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []

    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

# print(generate_n_bits(12))


def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1

    return d

''' One trial of 1000 samples'''
# d = binary_sampling_dict(num_bits=8, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


# ''' one trial of 100 samples '''
# d1 = binary_sampling_dict(num_bits=16, num_samples=100)

# for k, v in sorted(d1.items()):
#     print(f'{k}: {v / sum(d1.values())}')


# ''' one trial of 1000 samples '''
# d2 = binary_sampling_dict(num_bits=16, num_samples=1000)

# for k, v in sorted(d2.items()):
#     print(f'{k}: {v / sum(d2.values())}')



