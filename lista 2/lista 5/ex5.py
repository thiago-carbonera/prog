def xbox(height:int, width:int):
    for i in range(height):
        print('[', end='')
        for j in range(width*2-1):
            if j % 2 == 0:
                print('X', end='')
            else:
                print('-', end='')
        print(']')
    print()

def main():
    xbox(3,3)
    xbox(3, 6)
main()