import argparse
import itertools
import os

print_sums(f, S, k, mode)
    output = []
    mas = []

    for x in range(S+1):
        mas.append(x)
        for t in range(2, K+1):
            if x*t<=S and mode == 0:
                mas.append(x)
    for perm in itertools.permutations(mas, K):
        if sum(perm) == S:
            output.append(f"+".join(str(i) for i in perm))
    output = list(dict.fromkeys(output))
    try:
        print(f"{S}=" + "=".join(output))
        f.write(f"{S}=" + "=".join(output))
    except MemoryError:
        print("Not enough memory")
        file.close()
        exit(1)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', nargs="?", type=int, default=0)
    parser.add_argument('-K', nargs="?", type=int, default=0)
    parser.add_argument('-F', type=str, default="output1.txt")
    parser.add_argument('-NS', action='store_true', default=False)
    return parser


parser = create_parser()
namespace = parser.parse_args()
s, k = 1, 1

try:
    if namespace.S > 0:
        s = namespace.S
    else:
        print("Input S")
        s = int(input())

    if namespace.K > 0:
        k = namespace.K
    else:
        print("Input K")
        k = int(input())
except ValueError:
    print("smth wrong with data")
    exit(1)

filename = namespace.F
file = open(filename, "w")

mode = 1 if namespace.NS else 0
print_sums(file, s, k, mode)

finally:
    file.close()