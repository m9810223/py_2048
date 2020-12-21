from os import name as os_name
from os import system as os_system
from msvcrt import getch as msvcrt_getch
from G2048 import G2048


def clear_screen():
    _ = os_system('cls') if os_name == 'nt' else None
    _ = os_system('clear') if os_name == 'posix' else None


def move(g):
    def get_available_key():
        def key_ctl():
            t = msvcrt_getch()
            if t != b'\xe0':
                return t
            elif t == b'\xe0':
                t = msvcrt_getch()
                key = [b'H', b'P', b'K', b'M']
                d = dict(zip(key, ['up', 'down', 'left', 'right']))
                if t in d:
                    return d[t]
        k = key_ctl()
        while k not in ['up', 'down', 'left', 'right']:
            k = key_ctl()
        return k
    k = get_available_key()
    g.move(k)


def main():
    game = G2048(hig=4, wid=4, lv_win=11)
    clear_screen()
    print(game)
    while game.is_alive():
        move(g=game)
        clear_screen()
        print(game)
        if game.had_win:
            print('you win!')
            return
    print('game over!')


if __name__ == '__main__':

    main()
