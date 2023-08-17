def skewed_rect(height:int, width:int):
    for i in range(height):
        for empty in range(height):
            if empty < i:
                print('  ', end='')
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    skewed_rect(3, 3)
    skewed_rect(5, 4)
main()