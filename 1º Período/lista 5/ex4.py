def skewed_rect2(height:int, width:int):
    for i in range(height, 0, -1):
        for empty in range(height, 0, -1):
            if empty < i:
                print('  ', end='')
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    skewed_rect2(3, 3)
    skewed_rect2(5, 4)
main()