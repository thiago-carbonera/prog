def count_elements(vet:list):
    vet.sort()
    elements = []
    count = []
    for i in range(len(vet)):
        counter = 0

        if i == 0 or vet[i] != elements[-1]:
            elements.append(vet[i])

            for j in vet:
                if elements[-1] == j:
                    counter += 1

            count.append(counter)

    return count


def main():
    list = [1,2,3,4,4,5,4,3,6,7,3]
    print(count_elements(list))


if __name__ == '__main__':
    main()