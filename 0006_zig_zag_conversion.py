

# m * 1
# m * 2
input_string = "PAYPALISHIRING"
input_string = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."

len_s = len(input_string)

n = 2
m = 2 * n - 2

m1 = n
m2 = n - 2
n_blocks = (len_s // m) + 1
n_col = n_blocks * (n - 1)

zz_row = ["" for _ in range(n_col)]
zz_m   = [zz_row[:] for _ in range(n)]


for i, char in enumerate(input_string):
    
    block_number = i // (2 * n - 2)
    block_pos    = (i % (2 * n - 2)) + 1
    if block_pos <= n:
        row_number = block_pos - 1
        col_number = (block_number * (n - 1))
    else:
        row_number = n - (block_pos - n) - 1
        col_number = ((block_number * (n - 1)) + 1) + (block_pos - n) - 1
    zz_m[row_number][col_number] = char
    # print(f"{row_number=}, {col_number=}, {char=}")

# zz_m
out_str = ""

for row in zz_m:
    for char in row:
        if char != "":
            out_str += char

print(out_str)

