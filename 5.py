str_1 = input()
sym = input()
if str_1.find(sym) == str_1.rfind(sym):
    print(str_1.find(sym))
else:
    print(str_1.find(sym), ' ', str_1.rfind(sym))
