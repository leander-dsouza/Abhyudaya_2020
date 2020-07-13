def countSetBits(num):

    binary = bin(num)
    setBits = [ones for ones in binary[2:] if ones == '1']
    return len(setBits)


if __name__ == "__main__":
    n = int(input())

    for i in range(n+1):
        print(countSetBits(i), end =' ')
