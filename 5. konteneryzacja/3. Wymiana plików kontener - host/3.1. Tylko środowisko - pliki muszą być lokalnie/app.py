with open('input.txt') as f:
    lines = f.readlines()

print(lines)
triple_lines = 3 * lines
# Write lines to file
with open('output.txt', 'w') as f:
    f.writelines(triple_lines)