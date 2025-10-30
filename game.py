# Импорт пользовательского модуля из файла parts.py
# from parts import Board

# Импорт из пакета
from gameparts import Board
# Импорт собственных исключений
from gameparts.exceptions import FieldIndexError
from gameparts.exceptions import CellOccupiedError


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Первыми ходят крестики.
    current_player = "X"
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    # Отрисовать поле в терминале.
    print(game)
    game.display()

    while running:
        print(f"Ход делают {current_player}")

        # бесконечный цикл для обработки исключений
        while True:
            try:
                row = int(input("Введите номер строки: "))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                elif row is str:
                    raise ValueError
                column = int(input("Введите номер столбца: "))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                elif column is str:
                    raise ValueError
                if game.board[row][column] != " ":
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    "Значение должно быть неотрицательным и меньше "
                    f"{game.field_size}.\n"
                    "Пожалуйста, введите значения для строки и столбца заново."
                )
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

            except CellOccupiedError:
                print(
                    "Ячейка занята"
                    "Введите другие координаты."
                )
                continue

            except ValueError:
                print(
                    "Буквы вводить нельзя. Только числа.\n"
                    "Пожалуйста, введите значения для строки и столбца заново."
                )
                continue

            except Exception as e:
                print(f"Возникла ошибка: {e}")

            # Если в блоке try исключения не возникло...
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        game.make_move(row, column, current_player)
        print("Ход сделан!\n" + "-" * 5)
        game.display()

        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        if not running:
            game.save_result(current_player)

        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = "O" if current_player == "X" else "X"

    # Вывод докстирга класса Board
    # print("\n" + Board.__doc__)


# выполнять этот код, только если программа запущена напрямую
if __name__ == "__main__":
    main()
