
# buttons = []
# for i in range(1, 11):
#     button = 'Button {}'.format(i)
#     buttons.append(button)
#
# print(buttons)

buttons = ['Button {}'.format(i) for i in range(1, 11)]

positions = [(row, column) for row in range(2) for column in range(5)]


print(buttons)

print(positions)

