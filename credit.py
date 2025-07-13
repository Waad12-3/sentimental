from cs50 import get_int

def main():
    credit = get_int("Number: ")

    d_1 = 0
    d_2 = 0
    sum_1 = 0
    sum_2 = 0
    l = 0

    while credit > 0:
        d_2 = d_1
        d_1 = credit % 10

        if l % 2 == 0:
            sum_1 += d_1

        else:
            mul = 2 * d_1
            sum_2 += (mul // 10) + (mul % 10)

        credit //= 10
        l += 1

    check_sum = (sum_1 + sum_2) % 10 == 0
    ftd = (d_1 * 10) + d_2

    if ((ftd == 34 or ftd == 37) and (l == 15) and check_sum):
        print("AMEX")

    elif ((ftd >= 51 and ftd <= 55) and (l == 16) and check_sum):
        print("MASTERCARD")

    elif ((d_1 == 4) and ((l == 13 or l == 16)) and check_sum):
        print("VISA")

    else:
        print("INVALID")

if __name__ == "__main__":
    main()
