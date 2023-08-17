def centered_triangle(height:int):
    for i in range(height):
        for empty in range(height, 0, -1):
            if empty > i:
                print(' ', end='')
        for j in range(height-(height - i) + 1):
            print('🟧', end='')
        print()
    print()

def main():
    centered_triangle(6)
    centered_triangle(3)
main()