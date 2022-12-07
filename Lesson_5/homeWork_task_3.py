# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

my_text = 'AAaaaAdddLLkkKKfffffffKKDDnnrRR'

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

str_code = coding(my_text)
print(f"модуль сжатия: \nmy_text = {my_text}")
print(f"str_code =  {str_code}")

###########################

# my_text2 = '2A3a1A3d2L2k2K7f2K2D2n1r2R'
my_text2 = str_code

def decoding(txt):
    count = ''
    str_decode = ''
    for char in txt:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding(my_text2)

print(f"\nмодуль восстановления: \nmy_text2 = {my_text2}")
print(f"str_decode =  {str_decode}")