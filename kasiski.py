import argparse
import math

# Note: Unfinished (!)

def get_factors(n):    # (cf. https://stackoverflow.com/a/15703327/849891)
    j = 2
    while n > 1:
        for i in range(j, int(math.sqrt(n+0.05)) + 1):
            if n % i == 0:
                n /= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break


def decrypt(cipher):
    # Look for repeated strings between these lengths
    repeated_min = 3
    repeated_max = 10

    diffs = []
    for i in range(repeated_min, repeated_max +1):
        for j in range(0, len(cipher)):
            str1 = cipher[j:j+i]
            for k in range(0, len(cipher)):
                str2 = cipher[k:k+i]
                if str1 == str2 and j != k:
                    # Found a repeated string: add a possible key length
                    diffs.append(abs(k-j))

    diff_factors = []
    print(diffs)
    for diff in diffs:
        for factor in get_factors(diff):
            if factor != 1:
                diff_factors.append(factor)

    # Find modal value
    key_length = max(set(diff_factors), key=diff_factors.count)

    return key_length

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demystify")
    parser.add_argument("--ciphertext", type=str,
                        help="The ciphertext that is to be decrypted.")

    args = parser.parse_args()
    print(decrypt(args.ciphertext))
