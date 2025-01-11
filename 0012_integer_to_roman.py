

thousand_map = {
    1: 'M',
    2: 'MM',
    3: 'MMM',
    4: 'MMMM',
    5: 'MMMMM',
    6: 'MMMMMM',
    7: 'MMMMMMM',
    8: 'MMMMMMMM',
    9: 'MMMMMMMMM'
}

hundred_map = {
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM'
}

ten_map = {
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC'
}

one_map = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
}

x = 3749

# Output: "MMMDCCXLIX"

thousand_digit = x // 1000
thousand_remainder = x % 1000


hundred_digit = thousand_remainder // 100
hundred_remainder = thousand_remainder % 100


ten_digit = hundred_remainder // 10
ten_remainder = hundred_remainder % 10

one_digit = ten_remainder

output = thousand_map[thousand_digit] + hundred_map[hundred_digit] + ten_map[ten_digit] + one_map[one_digit]


print(thousand_digit)
print(thousand_remainder)
print(hundred_digit)
print(hundred_remainder)
print(ten_digit)
print(ten_remainder)
print(one_digit)

print(output)













