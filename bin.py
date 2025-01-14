def dec_to_bin(num, prec=32):
    bin = ""
    frac = num % 1

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


def bin_to_dec(bin: str):
    pass


print(dec_to_bin(580.976, 29))
