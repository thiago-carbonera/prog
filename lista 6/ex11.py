def find_min_max(vet:list) -> tuple[int, int]:
    vet.sort()
    higher = vet[0]
    smaller = vet[-1]
    return higher, smaller

def main():
    print(find_min_max([1,2,56,7,8]))
    print(find_min_max([-13,-14,-13,-56,-67,-86]))

if __name__ == '__main__':
    main()