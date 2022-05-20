import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow

COMBINATION = {
    1: [(0, 1)],
    2: [(0, 0, 1, 1),
        (0, 1, 0, 1)],
    3: [(0, 0, 0, 1, 1, 1, 0, 1),
        (0, 1, 0, 0, 1, 0, 1, 1),
        (0, 0, 1, 0, 0, 1, 1, 1)]
}


def xor_logic(a, b) -> bool:
    return bool(a) != bool(b)


def and_logic(a, b) -> bool:
    return a and b


def or_logic(a, b) -> bool:
    return a or b


def not_logic(a) -> bool:
    return not a


def translate_to_python(row: str) -> str:
    if '(' not in row:
        return replace_all(row)
    while '(' in row:
        if row.count('(') == 1:
            start = row.index('(')
            end = row.rindex(')')
        else:
            end = row.index(')')
            start = row.rindex('(', 0, end)
        replaced = translate_to_python(row[start + 1: end])
        row = row[:start] + replaced + row[end + 1:]
    return row


def replace_all(row: str) -> str:
    if '⊕' in row:
        index = row.index('⊕')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"xor[{left}, {right}]"
    if '|' in row:
        index = row.index('|')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"not[and[{left}, {right}]]"
    if '~' in row:
        index = row.index('~')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"not[xor[{left}, {right}]]"
    if '↓' in row:
        index = row.index('↓')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"not[or[{left}, {right}]]"
    if '→' in row:
        index = row.index('→')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"or[not[{left}], {right}]"
    if '∨' in row:
        index = row.index('∨')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"or[{left}, {right}]"
    if '∧' in row:
        index = row.index('∧')
        left = row[:index]
        if '̅' in left:
            left = f'not[{left[:-1]}]'
        right = row[index + 1:]
        if '̅' in right:
            right = f'not[{right[1:]}]'
        return f"and[{left}, {right}]"
    return 'not[' + row[:-1] + ']'


def get_vars(row: str):
    row = row.replace('xor', '').replace('and', '').replace('or', '').replace('not', '').replace('(', '')\
             .replace(')', '').replace(',', '').replace(' ', '')
    return list(set(row))


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.lineEdit
        # self.temp = self.ui.lbl_temp
        self.entry_max_len = self.entry.maxLength()

        # braces
        self.ui.btn_brace_left.clicked.connect(self.add_symbol)
        self.ui.btn_brace_right.clicked.connect(self.add_symbol)
        # operators
        self.ui.btn_arr_down.clicked.connect(self.add_symbol)
        self.ui.btn_arr_right.clicked.connect(self.add_symbol)
        self.ui.btn_eq.clicked.connect(self.add_symbol)
        self.ui.btn_xor.clicked.connect(self.add_symbol)
        self.ui.btn_or.clicked.connect(self.add_symbol)
        self.ui.btn_or_2.clicked.connect(self.add_symbol)
        self.ui.btn_sheff.clicked.connect(self.add_symbol)
        # vars
        self.ui.btn_x.clicked.connect(self.add_symbol)
        self.ui.btn_y.clicked.connect(self.add_symbol)
        self.ui.btn_z.clicked.connect(self.add_symbol)
        self.ui.btn_a.clicked.connect(self.add_symbol)
        self.ui.btn_b.clicked.connect(self.add_symbol)
        self.ui.btn_c.clicked.connect(self.add_symbol)
        self.ui.btn_d.clicked.connect(self.add_symbol)
        # actions
        self.ui.btn_ce.clicked.connect(self.clear_all)
        self.ui.btn_clear.clicked.connect(self.backspace)
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_not.clicked.connect(self.negate)

    def negate(self):
        entry = self.entry.text()

        allowed = list('XYZabcdxyzABCD')

        if len(entry) == 0:
            return

        if self.ui.lineEdit.text()[-1] in allowed:
            self.entry.setText(entry + '̅')

    def add_symbol(self):
        btn = self.sender()

        digit_buttons = ('btn_brace_left', 'btn_brace_right', 'btn_arr_down', 'btn_arr_right', 'btn_x',
                         'btn_y', 'btn_z', 'btn_a', 'btn_b', 'btn_d', 'btn_c', 'btn_eq', 'btn_sheff',
                         'btn_or_2', 'btn_or', 'btn_xor')

        if btn.objectName() in digit_buttons:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

    def calculate(self) -> None:
        value = self.ui.lineEdit.text()
        value = '(' + value + ')'
        result = translate_to_python(value).replace('[', '(').replace(']', ')')
        vars = get_vars(result)
        result = result.replace('xor', 'temp').replace('and', 'and_logic').replace('or', 'or_logic')\
                       .replace('not', 'not_logic').replace('temp', 'xor_logic')
        print(result)
        if len(vars) > 3:
            raise BaseException
        start_table_rows = list(zip(vars, COMBINATION[len(vars)]))
        print(start_table_rows)


    def clear_all(self) -> None:
        self.entry.setText('')

    def backspace(self) -> None:
        entry = self.entry.text()

        if len(entry) == 0:
            return

        self.entry.setText(entry[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
