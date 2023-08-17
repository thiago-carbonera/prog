def main():
    v1 = [1, 2, 3, 4, 5, 8, 2]
    #v1[3] = 9999
    #idx = v1.index(8)
    #print(idx)

    for i in range(len(v1)):
        print(f"{v1[i]}--", end='')
    print("\b\b  ")

if __name__=="__main__":
    main()