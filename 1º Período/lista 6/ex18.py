def min_bills(value:int, notes:list):
    idx = -1
    counter = 0
    while value > 0:
        if value - notes[idx] >= 0:
            value -= notes[idx]
            counter += 1
        else:
            print(f'{counter} X {notes[idx]}$')
            idx -= 1
            counter = 0
    print(f'{counter} X {notes[idx]}$')


def main():
    notes = [1,2,5,10,20,50,100,200]
    min_bills(5229, notes)

if __name__ == '__main__':
    main()