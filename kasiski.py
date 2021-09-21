import argparse

def decrypt(cipher):
    # Look for repeated strings between these lengths
    repeated_min = 3
    repeated_max = 10

    for i in range(repeated_min, repeated_max +1):
        for j in range(0, len(cipher)):
            str1 = cipher[j:j+i]
            for k in range(0, len(cipher)):
                str2 = cipher[k:k+i]
                if str1 == str2 and j != k:
                    print("repeated string: " + str1)
    return cipher

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demystify")
    parser.add_argument("--ciphertext", type=str,
                        help="The ciphertext that is to be decrypted.")

    args = parser.parse_args()
    print(decrypt(args.ciphertext))
