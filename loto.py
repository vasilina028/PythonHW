import random
from typing import List, Dict, Set


class Card:
    def __init__(self):
        self.rows: List[List[str]] = []
        self.numbers: Set[int] = set()
        self.generate_card()

    def generate_card(self):
        # Генерируем 15 уникальных чисел для карточки
        all_numbers = random.sample(range(1, 91), 15)

        # Разбиваем на 3 строки по 5 чисел и сортируем каждую строку
        row1_numbers = sorted(all_numbers[:5])
        row2_numbers = sorted(all_numbers[5:10])
        row3_numbers = sorted(all_numbers[10:15])

        # Создаем строки карточки
        self.rows.append(self._create_row(row1_numbers))
        self.rows.append(self._create_row(row2_numbers))
        self.rows.append(self._create_row(row3_numbers))

        # Сохраняем все числа карточки
        self.numbers = set(all_numbers)

    def _create_row(self, numbers: List[int]) -> List[str]:
        row = [' -'] * 9  # Все клетки изначально пустые
        positions = random.sample(range(9), 5)  # 5 случайных позиций для чисел
        positions.sort()  # Сортируем позиции для порядка слева направо

        for num, pos in zip(numbers, positions):
            row[pos] = f"{num:2}"  # Заполняем выбранные позиции числами

        return row

    def has_number(self, number: int) -> bool:
        return number in self.numbers

    def cross_out(self, number: int) -> bool:
        if number in self.numbers:
            self.numbers.remove(number)
            # Заменяем число на ' X' во всех строках
            for row in self.rows:
                for i in range(len(row)):
                    if row[i].strip() == str(number):
                        row[i] = ' X'
            return True
        return False

    def is_empty(self) -> bool:
        return len(self.numbers) == 0

    def display(self, title: str) -> str:
        lines = [f"--- {title} ---"]
        for row in self.rows:
            line = ' '.join(num for num in row)
            lines.append(line)
        lines.append('-' * 25)
        return '\n'.join(lines)

    def is_empty(self) -> bool:
        return len(self.numbers) == 0

    def display(self, title: str) -> str:
        lines = [f"--- {title} ---"]
        for row in self.rows:
            line = ' '.join(f"{num:>2}" if num else '  ' for num in row)
            lines.append(line)
        lines.append('-' * 25)
        return '\n'.join(lines)


class Barrel:
    def __init__(self):
        self.remaining_numbers: List[int] = list(range(1, 91))
        random.shuffle(self.remaining_numbers)
        self.drawn_numbers: Set[int] = set()

    def draw(self) -> int:
        if not self.remaining_numbers:
            raise ValueError("No more barrels left!")
        number = self.remaining_numbers.pop()
        self.drawn_numbers.add(number)
        return number

    def count_remaining(self) -> int:
        return len(self.remaining_numbers)


class Player:
    def __init__(self, name: str, is_computer: bool = False):
        self.name = name
        self.is_computer = is_computer
        self.card = Card()

    def make_decision(self, number: int) -> bool:
        if self.is_computer:
            return self.card.has_number(number)
        else:
            return self._ask_player(number)

    def _ask_player(self, number: int) -> bool:
        while True:
            answer = input("Зачеркнуть цифру? (y/n): ").lower()
            if answer in ('y', 'n'):
                return answer == 'y'


class Game:
    def __init__(self):
        self.player = Player("Ваша карточка")
        self.computer = Player("Карточка компьютера", is_computer=True)
        self.barrel = Barrel()
        self.game_over = False
        self.winner = None

    def start(self):
        print("Игра Лото началась!")

        while not self.game_over and self.barrel.count_remaining() > 0:
            self._play_round()

        self._end_game()

    def _play_round(self):
        # Достаем новый бочонок
        number = self.barrel.draw()
        remaining = self.barrel.count_remaining()
        print(f"\nНовый бочонок: {number} (осталось {remaining})")

        # Показываем карточки
        print(self.player.card.display("Ваша карточка"))
        print(self.computer.card.display("Карточка компьютера"))

        # Ход игрока
        player_decision = self.player.make_decision(number)
        if player_decision:
            if not self.player.card.cross_out(number):
                print(f"Числа {number} нет на вашей карточке! Вы проиграли.")
                self.game_over = True
                self.winner = "computer"
                return
        else:
            if self.player.card.has_number(number):
                print(f"Вы пропустили число {number}, которое есть на вашей карточке! Вы проиграли.")
                self.game_over = True
                self.winner = "computer"
                return

        # Ход компьютера
        if self.computer.card.has_number(number):
            self.computer.card.cross_out(number)

        # Проверяем победу
        if self.player.card.is_empty():
            self.game_over = True
            self.winner = "player"
        elif self.computer.card.is_empty():
            self.game_over = True
            self.winner = "computer"

    def _end_game(self):
        print("\nИгра окончена!")
        if self.winner == "player":
            print("Поздравляем! Вы выиграли!")
        elif self.winner == "computer":
            print("Компьютер выиграл. Попробуйте еще раз!")
        else:
            print("Игра завершена без победителя.")


if __name__ == "__main__":
    game = Game()
    game.start()