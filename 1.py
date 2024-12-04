def largest(debug=False):
    '''
    Функция для нахождения наибольшего числа из numbers.txt.
    Args:
        debug=False: boolean; Режим отладки
    Returns:
        int
    '''
    with open(['', '_test_'][debug] + 'numbers.txt', 'r', encoding='utf-8') as f:
        data = map(int, f.read().split())
        if debug:
            print(data)
        return max(data)