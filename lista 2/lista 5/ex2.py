'''
Exercício 2
'''
def rect(height:int, width:int):
    for i in range(height):
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    rect(3, 4)
    rect(5, 5)
main()

