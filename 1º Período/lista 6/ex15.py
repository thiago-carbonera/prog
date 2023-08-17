def remove_all(vet:list, elem:int):
    index = 0
    while index < len(vet):
        if vet[index] == elem:
            vet.pop(index)
            index -= 1
        index += 1

def main():
    list = [1,2,3,4,5,6,7,6,5,8,9]
    print(list)
    remove_all(list, 5)
    print(list)
    remove_all(list, 3)
    print(list)

if __name__ == '__main__':
    main()