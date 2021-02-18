from random import choice

def get_bit():
    return choice([0,1])

def generate_binary(n=8):
    return [get_bit() for bit in range(n)]

