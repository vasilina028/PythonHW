class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"- Name: {self.name}\n- Age: {self.age}\n- Position: {self.position}"


class Team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            print(f"Игрок {player.name} добавлен в команду {self.team_name}")
        else:
            print(f"Игрок {player.name} уже в команде {self.team_name}")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Игрок {player.name} удален из команды {self.team_name}")
        else:
            print(f"Игрок {player.name} не найден в команде {self.team_name}")

    def list_players(self):
        print(f"\nКоманда: {self.team_name}")
        print(f"Тренер: {self.coach}")
        print("Состав игроков:")
        if not self.players:
            print("В команде нет игроков")
        else:
            for player in self.players:
                print(player)
                print()  # Пустая строка между игроками


# Пример использования
if __name__ == "__main__":
    # Создаем игроков
    player1 = Player("Иванов", 25, "Нападающий")
    player2 = Player("Петров", 30, "Полузащитник")
    player3 = Player("Сидоров", 28, "Защитник")

    # Создаем команды
    team1 = Team("Красные", "Краснов")
    team2 = Team("Синие", "Синёв")

    # Добавляем игроков в команды
    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    # Выводим список игроков в командах
    team1.list_players()
    team2.list_players()

    # Удаляем игрока из команды
    team1.remove_player(player2)

    # Выводим обновленный список игроков
    team1.list_players()