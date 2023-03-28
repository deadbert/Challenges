def conv_to_bin(num):
    bin_backward = ''
    while num > 0:
        bin_backward = bin_backward + str(num%2)
        num = num // 2
    bin_number = bin_backward[::-1]
    return bin_number


print(conv_to_bin(200))

