def right_triangle(size:int):
    for i in range(size):
        for empty in range(size):
            if empty < i:
                print('  ', end='')
        for j in range(size-i):
            print('🟧', end='')
        print()
    print()

def main():
    right_triangle(5)
main()