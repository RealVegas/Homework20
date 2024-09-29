from abc import ABC, abstractmethod


class Weapon(ABC):
    weapon_name = None

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    weapon_name: str = 'Меч'

    def attack(self) -> None:
        print('Ударил мечом')


class Bow(Weapon):
    weapon_name: str = 'Лук'

    def attack(self) -> None:
        print('Пустил стрелу')


class Fighter:
    def __init__(self) -> None:
        self.weapon = None

    def change_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f'Боец выбрал {weapon.weapon_name}')

    def attack(self) -> None:
        self.weapon.attack()


class Monster:
    @classmethod
    def attacked(cls) -> None:
        print('Монстр повержен')


# Программа
warrior = Fighter()
monster = Monster()

warrior.change_weapon(Sword())
warrior.attack()
monster.attacked()
print()
warrior.change_weapon(Bow())
warrior.attack()
monster.attacked()