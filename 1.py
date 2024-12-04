def largest():
    '''
    Функция для нахождения наибольшего числа из numbers.txt.
    Args:
        None
    Returns:
        int
    '''
    with open('numbers.txt', 'r', encoding='utf-8') as f:
        data = map(int, f.read().split())
        return max(data)