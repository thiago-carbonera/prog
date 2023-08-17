def reverse_list(vet:list):
    for i in range(len(vet)//2):
        vet[i], vet[-(i+1)] = vet[-(i+1)], vet[i]


def main():
    vet = [1,2,3,4]
    print(vet)
    reverse_list(vet)
    print(vet)
    vet = [1,2,3,4,5]
    print(vet)
    reverse_list(vet)
    print(vet)


if __name__ == '__main__':
    main()
