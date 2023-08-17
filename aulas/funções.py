'''
funções
'''

def print_ascii(col):
    for i in range(col):
        print("DEC OCT HEX CHR   ", end="")
        print()

    n = 94 // col
    c = 33

    for i in range(n):
        for j in range(col):
            idx = c + n * j
            if idx > 126:
                break
            print(f"{idx} {oct(idx)} {hex(idx)} {chr(idx)}   ", edn="")
        print()
        c += 1


def main():
    print_ascii(4)

main()