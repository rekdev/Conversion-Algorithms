def dec_to_bin(num, prec=32):
    bin = ""
    frac = num % 1
    num = int(num)

    while num > 0:
        bin = ("0" if num % 2 == 0 else "1") + bin

        num = num // 2

    if not frac == 0:
        bin += "."
        count = 0

        while not count == prec:
            frac *= 2
            bin += "1" if frac > 1 else "0"

            frac = frac % 1
            count += 1

    return bin


def bin_to_dec(bin):
    num = 0

    if "." in bin:
        intg, frac = bin.split(".")
    else:
        intg, frac = bin, None

    intg = list(intg)
    frac = list(frac) if not frac == None else frac

    for i in range(len(intg) - 1, -1, -1):
        num += ((2**(len(intg)-1-i)) * int(intg[i]))

    return num


print(dec_to_bin(580.970, 29))
print(bin_to_dec("1001000100"))
