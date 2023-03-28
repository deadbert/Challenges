
def hide_card(num):
    num = str(num)
    hidden_card = ''
    for x in range(len(num)-4):
        hidden_card += '*'
    hidden_card = hidden_card + num[-4:]
    return hidden_card


print(hide_card(123456789))
