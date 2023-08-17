def run_menu():
    option = int()
    a = int()
    b = int()
    while option != 5:
        print(f'''
--------------------------------------------------
SUPREME SUM! A: {a} B: {b}
--------------------------------------------------
1 - Set A
2 - Set B
3 - Show A+B
4 - Show AxB
5 - Exit
              ''')
        option = int(input('Select an option: '))
        if option == 1:
            a = int(input('Set A:'))
        elif option == 2:
            b = int(input('Set B: '))
        elif option == 3:
            print(a+b)
        elif option == 4:
            print(a*b)

def main():
    run_menu()
main()