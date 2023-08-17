def histogram(days:list):
    for e in days:
        if e < 0:
            e *= -1
        print('>'*e)

def main():
    histogram([5,8,12,11,10,7,-1])

if __name__ == '__main__':
    main()