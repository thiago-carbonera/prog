def floyd(size):
    counter = 1
    for i in range(1, size+1):
        for j in range(i):
            print(counter, end=' ')
            counter += 1
        print()

def main():
    floyd(6)
main()