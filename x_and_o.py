def x_compare(x_o_list):
    x_count = 0
    o_count = 0
    for item in x_o_list:
        if item == 'x':
            x_count += 1
        elif item == 'o':
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False

print(x_compare(['x','o','y','p']))