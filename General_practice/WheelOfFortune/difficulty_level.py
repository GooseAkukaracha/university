lifes: int = 0
set_difficult: bool = False

def count_life() -> int:
    """
    :return: количество жизней в зависимости от выбора уровня сложности
    """
    choice: int = int(input('Введите уровень сложности: 1-легко, 2-средне, 3-сложно '))

    if choice == 1:
        return 10
    elif choice == 2:
        return 6
    elif choice == 3:
        return 4
    else:
        print('Вы не ввели уровень сложности!')
        return count_life()
