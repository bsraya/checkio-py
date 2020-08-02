def even_the_last(array: list) -> int:
    total = 0
    if(len(array)==0): return 0
    for index in range(0, len(array)):
        if(index % 2 == 0):
            total = total + array[index]
    total = total * array[-1]
    return total

if __name__ == '__main__':
    print('Example:')
    print(even_the_last([0, 1, 2, 3, 4, 5]))
    
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_the_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_the_last([6]) == 36, "(6)*6=36"
    assert even_the_last([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")