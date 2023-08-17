def histogram(days:list):
    for e in days:
        if e < 0:
            e *= -1
        print('>'*e)

def temperature_report(days:list):
    higher = -float("inf")
    smaller = float("inf")
    average = 0
    for e in days:
        if e > higher:
            higher = e
        elif e < smaller:
            smaller = e
        average += e
    average /= 7
    print(f'Average:{average:.3}; Max:{higher}; Min:{smaller}')
    histogram(days)



def main():
    temperature_report([5,8,12,11,10,7,-1])

if __name__ == '__main__':
    main()