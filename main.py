from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """
    Calculate damage by a character class.

    Keywords arguments:
    char_name -- player's name
    char_class -- player's  class
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(-3, -1)}')
    return


def defence(char_name: str, char_class: str) -> str:
    """
    Calculate amount of damage blocked.

    Keywords arguments:
    char_name -- player's name
    char_class -- player's  class
    """
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    """
    Activate special ability.

    Keywords arguments:
    char_name -- player's name
    char_class -- player's  class
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """
    Start training.
    Players can try there difference game mechanics there.

    Keywords arguments:
    char_name -- player's name
    char_class -- player's  class
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Invite the player to select a game class."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого '
                           'хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или '
                               'любую другую кнопку, чтобы выбрать '
                               'другого персонажа ').lower()
    return char_class


# Тестовые данные.
TEST_DATA: list[tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """
    Add some reputation points to the player.

    Keywords arguments:
    current_rep -- current value
    rep_points -- how many points to add
    buf_effect -- bonus status

    """
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float, rep_points: int,
               debuf_effect: bool) -> float:
    """
    Substracts some points from players'.

    Keywords arguments:
    current_rep -- current value
    rep_points -- how many points to add
    debuf_effect -- debuff status
    """
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
