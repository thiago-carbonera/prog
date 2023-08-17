def remove_all(vet:list, elem:int):
    for i in range(len(vet)):
        try:
            vet.remove(elem)
        except:
            pass

def main():
    list = [1,2,3,4,5,6,7,6,5,8,9]
    print(list)
    remove_all(list, 5)
    print(list)
    remove_all(list, 3)
    print(list)

if __name__ == '__main__':
    main()
