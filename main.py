from clases import Hero, Game

def main():
    player = Hero('Человеческий детеныш')
    computer = Hero('Бездушный компьютер')
    quit = True
    while quit:
        print('Смертельная битва началсь')
        current_game = Game(player, computer)
        current_game.start()
        quit_ask = input('Еще одна игра? (y) :')
        if quit_ask != 'y' or quit_ask != 'Y':
            quit = False
if __name__ == '__main__':
    main()
