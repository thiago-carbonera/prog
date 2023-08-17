def find_max2(vet:list) -> int:
    higher = -float("inf")
    for e in vet:
        if higher < e:
            higher = e
    return higher

def main():
    print(find_max2([1,2,56,7,8]))
    print(find_max2([-13,-14,-13,-56,-67,-86]))

if __name__ == '__main__':
    main()