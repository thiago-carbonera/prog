'''
Exercício 1
'''
def mult_table():
    print('-------------')
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i: >2} X {j: >2} = {(i*j): >2}')
        print('-------------')

def main():
    mult_table()
main()