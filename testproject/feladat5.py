with open('data.txt', 'r', encoding="UTF-8") as f:
    txt_lines = f.readlines()
    print(type(txt_lines))
    print(txt_lines)

print('--------')
for s in txt_lines:
    print(s, end='')
