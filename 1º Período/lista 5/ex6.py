def box(height:int, width:int):
    for i in range(1, height+1):
        for j in range(1, width+1):
            if i == 1 or i == height:
                if j == 1 or j == width:
                    print('+', end='')
                else:
                    print('-', end='')
            else:
                if j == 1 or j == width:
                    print('|', end='')
                else:
                    print(' ', end='')
        print()

def main():
    box(5, 10)
main()