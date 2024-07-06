from abc import ABC, abstractmethod
from random import random


class Character(ABC):
    @abstractmethod
    def attack(self,someone):
        pass
    def is_alive(self):
        pass


class Hero(Character):
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        current_attack = round(self.attack_power*random(), 1)
        print(f'Игрок {self.name} атакует {other.name} c силой {current_attack} единиц атаки')
        other.health -= current_attack
        print(f'У игрока {other.name} осталось {other.health:.1f} единиц здоровья')
    def is_alive(self):
        if self.health < 0:
            return False
        return True

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        # Определяем, чей ход первый
        if random() >= 0.5:
            player_first = self.player
            player_second = self.computer
            player_first_flag = True
        else:
            player_first = self.computer
            player_second = self.player
            player_first_flag = False
        print(f'Игроку {player_first.name} повезло - он ходит первым')
        while True:
            player_first.attack(player_second)
            if not(player_second.is_alive()):
                print(f'Игрок {player_second.name} уничтожен')
                print(f'Игрок {player_first.name} победил')
                break
            player_second.attack(player_first)
            if not(player_first.is_alive()):
                print(f'Игрок {player_first.name} уничтожен')
                print(f'Игрок {player_second.name} победил')
                break
        if player_first_flag:
            self.player = player_first
            self.computer = player_second
        else:
            self.player = player_second
            self.computer = player_first
