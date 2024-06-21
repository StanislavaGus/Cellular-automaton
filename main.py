import random
import tkinter as tk

"""
    Генерирует клеточное поле и отображает его на экране.

    Входные аргументы:
        None

    Выходные аргументы:
        None

    Функция получает размер поля от пользователя через поле ввода и создает клеточное поле с 
    указанными размерами. Если введенное значение не является положительным целым числом, 
    выводит сообщение об ошибке.
    """
def generate_grid():
    global rows, cols, grid, cell_size, grid_values, pause, iter_num
    start_button["state"] = tk.NORMAL
    pause_button.config(text="Пауза")
    pause = False
    iter_num = 100

    try:
        field_size = int(entry.get())
        if field_size > 0:
            result_label.config(text="")
            rows = cols = field_size
            cell_size = min(width // cols, height // rows)
            grid_values = [[0]*cols for _ in range(rows)]

            if not is_checked:
                grid = [[white] * cols for _ in range(rows)]

            else:
                grid_values = [[random.randint(0, 1) for _ in range(cols)]
                               for _ in range(rows)]
                grid = [[white if grid_values == 0 else black for grid_values in row]
                        for row in grid_values]

            draw_grid()

        else:
            result_label.config(text="число должно быть положительным")
    except ValueError as e:
            result_label.config(text="введено некорректное значение")


my_Rule = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
           0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1,
           1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
actual_Rule = [0]*32
iter_num = 100



# Размеры и параметры клеочного поля по умолчанию
rows, cols = 30, 30
cell_size = 20
width, height = cell_size * cols, cell_size * rows


# Инициализация окна Tkinter
root = tk.Tk()
root.title("Клеточное поле")

# Инициализация цветов
white = "#ffffff"
black = "#000000"

# Создание Canvas для отображения клеточного поля
canvas = tk.Canvas(root, width=width, height=height, bg=white)
canvas.pack()

# Создание двумерного массива для хранения цветов ячеек
grid = [[white] * cols for _ in range(rows)]
grid_values = [[0] * cols for _ in range(rows)]


"""
    Обрабатывает событие клика мыши на клеточном поле.

    Входные аргументы:
        event (tk.Event): Событие клика мыши.

    Выходные аргументы:
        None

    Функция определяет координаты клика мыши и изменяет состояние клетки в соответствии 
    с цветом (черным или белым).
    """
def cell_click(event):
    global grid_values, grid
    col = event.x // cell_size
    row = event.y // cell_size
    if grid[row][col] == white:
        grid_values[row][col] = 1
        grid[row][col] = black
    else:
        grid[row][col] = white
        grid_values[row][col] = 0
    draw_grid()

"""
    Отображает клеточное поле на экране.

    Входные аргументы:
        None

    Выходные аргументы:
        None

    Функция проходит по всем клеткам поля и отрисовывает их на холсте с заданными цветами.
    """
def draw_grid():
    canvas.delete("all")
    for row in range(rows):
        for col in range(cols):
            canvas.create_rectangle(col * cell_size, row * cell_size,
                                    (col + 1) * cell_size, (row + 1) * cell_size,
                                    fill=grid[row][col], outline="gray")



# Привязка функции к событию клика мыши
canvas.bind("<Button-1>", cell_click)

# Создание и размещение элементов интерфейса
entry_label = tk.Label(root, text="Введите размер поля:")
entry_label.pack()
entry_label.place(x=950, y=20)

entry = tk.Entry(root)
entry.pack()
entry.place(x=950, y=50)

result_label = tk.Label(root, text="")
result_label.pack()
result_label.place(x=950, y=70)

generate_button = tk.Button(root, text="Сгенерировать поле", command=generate_grid)
generate_button.pack()
generate_button.place(x=950, y=250)

#------------------------------------
def toggle_state():
    global is_checked
    is_checked = not is_checked
    update_display()

def update_display():
    if is_checked:
        label_Avt_Gen.config(text="Поле задается автоматически \n "
                                  "(нажмите для смены режима)", bg="white")
    else:
        label_Avt_Gen.config(text="Поле задается вручную \n (нажмите для смены режима)",
                             bg="white")

# Глобальная переменная для отслеживания состояния поля (отмечено или нет)
is_checked: bool = False

# Инициализация окна Tkinter
root.title("Интерактивное поле")

# Создание метки для отображения состояния поля
label_Avt_Gen = tk.Label(root, text="Поле задается вручную \n (нажмите для смены режима)",
                         font=("Arial", 8), width=26, height=3, bg="white")
label_Avt_Gen.pack(padx=10, pady=10)
label_Avt_Gen.place(x=950, y=100)

optimal_num_label = tk.Label(root, text="Введите номер для\nоптимальной реализации:")
optimal_num_label.pack()
optimal_num_label.place(x=950, y=160)

entry_num = tk.Entry(root)
entry_num.pack()
entry_num.place(x=950, y=205)

result_label2 = tk.Label(root, text="")
result_label2.pack()
result_label2.place(x=950, y=225)

# Привязка функции к событию клика мыши
label_Avt_Gen.bind("<Button-1>", lambda event: toggle_state())

#------------------------------------

pause: bool = False
def switch_pause_state():
    global pause
    pause = not pause
    if pause:
        pause_button.config(text="Продолжить")
    else:
        pause_button.config(text="Пауза")
        start_program()


pause_button = tk.Button(root, text="Пауза", command=switch_pause_state, state=tk.DISABLED)
pause_button.pack()
pause_button.place(x=950, y=330)


def transfer_to_binary(decimal_number):
    binary_array = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_array.insert(0, remainder)  # Вставляем остаток в начало массива
        decimal_number //= 2

    # Если исходное число было 0, добавляем 0 в массив
    if not binary_array:
        binary_array.append(0)
    return binary_array

"""
    Запускает программу с заданными правилами игры "Жизнь".

    Входные аргументы:
        None

    Выходные аргументы:
        None

    Функция начинает выполнение программы с заданными пользователем правилами игры "Жизнь".
    """
def start_program():
    global pause, actual_Rule, my_Rule, grid_values, grid, iter_num

    try:
        enter_flag = True
        if entry_num.get() != "":
            enter_flag = False
        rule = 1
        if not enter_flag:
            rule = int(entry_num.get())
        if (rule >= 0):
            result_label2.config(text="")
            pause_button["state"] = tk.NORMAL
            start_button["state"] = tk.DISABLED

            if entry_num.get() != "":
                new_arr = transfer_to_binary(rule)

                # обнуляем массив с правилом массив фиксированной длины 32
                if len(new_arr) > 32:
                    actual_Rule = [0] * 32
                    # Копируем значения из new_arr в tmp_array
                    start_index = max(0, len(new_arr) - 32)
                    for i in range(32):
                        if start_index + i < len(new_arr):
                            actual_Rule[i] = new_arr[start_index + i]

                elif len(new_arr) < 32:
                    actual_Rule = [0] * (32 - len(new_arr)) + new_arr[-32:]

                else:
                    actual_Rule = new_arr

                # Вывод результата
                print("Исходный массив:", new_arr)
                print("Новый массив:", actual_Rule)

            else:
                actual_Rule = my_Rule

            """
                Обновляет состояние клеточного поля в соответствии с правилами игры "Жизнь".

                Входные аргументы:
                    None

                Выходные аргументы:
                    None

                Функция обновляет состояние каждой клетки поля в соответствии с 
                правилами игры "Жизнь".
                """
            def update():
                global grid_values, grid, iter_num
                if not pause:
                    tmp_grid_values = grid_values
                    cell_1 = cell_2 = cell_3 = cell_4 = cell_5 = 0
                    for i in range(rows - 1):
                        for j in range(cols - 1):
                            # print(i," ",j)
                            # центральная
                            cell_5 = grid_values[i][j]

                            # верхняя
                            if i == 0:
                                cell_1 = grid_values[rows - 1][j]
                            else:
                                cell_1 = grid_values[i - 1][j]

                            # нижняя
                            if i == rows - 1:
                                cell_2 = grid_values[0][j]
                            else:
                                cell_2 = grid_values[i + 1][j]

                            # левая
                            if j == 0:
                                cell_3 = grid_values[i][cols - 1]
                            else:
                                cell_3 = grid_values[i][j - 1]

                            # правая
                            if i == rows - 1:
                                cell_4 = grid_values[i][0]
                            else:
                                cell_4 = grid_values[i][j + 1]

                            result_num = (cell_1 * 2 ** 4 + cell_2 * 2 ** 3 +
                                          cell_3 * 2 ** 2 + cell_4 * 2 ** 1
                                          + cell_5 * 2 ** 0)
                            result_value = actual_Rule[result_num - 1]

                            #grid_values[i][j] = result_value
                            tmp_grid_values[i][j] = result_value

                            if result_value == 0:
                                grid[i][j] = white
                            else:
                                grid[i][j] = black
                    grid_values = tmp_grid_values
                    draw_grid()

                    # Запланируйте следующее обновление через 500 миллисекунд (0.5 секунды)
                    if (iter_num):
                        iter_num = iter_num - 1
                        root.after(1000, update)

            # Запустите цикл обновлений
            update()

        else:
            result_label2.config(text="число должно быть положительным")
    except ValueError as e:
            result_label2.config(text="введено некорректное значение")


start_button = tk.Button(root, text="Запуск", command=start_program)
start_button.pack()
start_button.place(x=950, y=300)


# Отрисовка начального состояния клеточного поля
draw_grid()

# Запуск основного цикла Tkinter
root.mainloop()