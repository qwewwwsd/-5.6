class Game():
    # Переменные
    def __init__(self):
        self.FN = {
            '00': '-',
            '01': '-',
            '02': '-',
            '10': '-',
            '11': '-',
            '12': '-',
            '20': '-',
            '21': '-',
            '22': '-'
            }
        
        self.steps = 0
    
    # Игровое поле    
    def field(self):
        print(
            '\n ', '0', '1', '2',
            '\n0', self.FN['00'], self.FN['01'], self.FN['02'],
            '\n1', self.FN['10'], self.FN['11'], self.FN['12'],
            '\n2', self.FN['20'], self.FN['21'], self.FN['22']
              )
    # Правила
    def rules(self):
        print('\nКрестики-нолики\n\nПравила игры:\n1. Побеждает тот, у кого 3 крестика или нолика по горизонтальной или по вертикальной либо по диагональной линии.')
        print('2. Чтобы осуществить ход, нужно написать два номера клетки слитно (Пример: 21 - это ход на 3 линию в клетку по центру).')
        print('3. Ход игры - поочередно. Игра начинается крестиком.')
        print('4. Для выхода напишите "exit".')
    
    # Кто ходит
    def step(self):
        if self.steps % 2 == 0:
            return 'x'
        elif self.steps % 2 == 1:
            return 'o'
    
    # Проверка хода и замена клетки 
    def step_check(self, x):
        if x == 'exit':
            exit()
            
        try:
            self.FN[x]
        except KeyError:
            print('\n!!!Неверная клетка!!!')
        else:
            if self.step() == 'x':
                if self.FN[x] != 'x' and self.FN[x] != 'o':
                    self.FN[x] = 'x'
                    self.steps += 1
                else:
                    print('\n!!!Эта клетка уже занята!!!')
            elif self.step() == 'o':
                if self.FN[x] != 'o' and self.FN[x] != 'x':
                    self.FN[x] = 'o'
                    self.steps += 1
                else:
                    print('\n!!!Эта клетка уже занята!!!')
    
    # Нахождение победителя
    def winner_check(self):
        # x
        if self.FN['00'] == 'x' and self.FN['10'] == 'x' and self.FN['20'] == 'x':
            return 'win x'
        elif self.FN['01'] == 'x' and self.FN['11'] == 'x' and self.FN['21'] == 'x':
            return 'win x'
        elif self.FN['02'] == 'x' and self.FN['12'] == 'x' and self.FN['22'] == 'x':
            return 'win x'
        elif self.FN['20'] == 'x' and self.FN['21'] == 'x' and self.FN['22'] == 'x':
            return 'win x'
        elif self.FN['10'] == 'x' and self.FN['11'] == 'x' and self.FN['12'] == 'x':
            return 'win x'
        elif self.FN['00'] == 'x' and self.FN['01'] == 'x' and self.FN['02'] == 'x':
            return 'win x'
        elif self.FN['20'] == 'x' and self.FN['11'] == 'x' and self.FN['02'] == 'x':
            return 'win x'
        elif self.FN['00'] == 'x' and self.FN['11'] == 'x' and self.FN['22'] == 'x':
            return 'win x'
        # o
        if self.FN['00'] == 'o' and self.FN['10'] == 'o' and self.FN['20'] == 'o':
            return 'win o'
        elif self.FN['01'] == 'o' and self.FN['11'] == 'o' and self.FN['21'] == 'o':
            return 'win o'
        elif self.FN['02'] == 'o' and self.FN['12'] == 'o' and self.FN['22'] == 'o':
            return 'win o'
        elif self.FN['20'] == 'o' and self.FN['21'] == 'o' and self.FN['22'] == 'o':
            return 'win o'
        elif self.FN['10'] == 'o' and self.FN['11'] == 'o' and self.FN['12'] == 'o':
            return 'win o'
        elif self.FN['00'] == 'o' and self.FN['01'] == 'o' and self.FN['02'] == 'o':
            return 'win o'
        elif self.FN['20'] == 'o' and self.FN['11'] == 'o' and self.FN['02'] == 'o':
            return 'win o'
        elif self.FN['00'] == 'o' and self.FN['11'] == 'o' and self.FN['22'] == 'o':
            return 'win o'
    
    # Активация
    def activate(self):
        while True:
            if self.steps == 9:
                print('Игра окончена!')
                break
            elif self.winner_check() == 'win x':
                print('\n- Победил игрок за x\n')
                exit()
            elif self.winner_check() == 'win o':
                print('\n- Победил игрок за o\n')
                exit()
                
            self.field()
            if self.step() == 'x':
                print('Ход: x')
            elif self.step() == 'o':
                print('Ход: o')
                
            step = str(input('Пишите: '))
            self.step_check(step)
        
        
if __name__ == '__main__':
    start_question = input('Начанть игру? (N/y) ')
    if start_question == 'y':
        while True:
            Game().activate()
    else:
        exit()
        