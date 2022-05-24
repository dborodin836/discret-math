import sys
from typing import List, Tuple

from PySide6.QtWidgets import QApplication, QMainWindow
from prettytable import PrettyTable
from loguru import logger

from design import Ui_MainWindow


def get_combinations(no: int):
    result = [(0, 1)]
    while len(result) != no:
        for element, index in zip(result, range(len(result))):
            result[index] = element + element[::-1]
        length = len(result[0]) // 2
        tuple_ = (0, ) * length + (1, ) * length
        result.append(tuple_)
    return result


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
    """
    Replaces all math symbols to functions_names.
    """
    symbols = [('⊕', "xor[%s, %s]"), ('|', "not[and[%s, %s]]"), ('~', "not[xor[%s, %s]]"),
               ('↓', "not[or[%s, %s]]"), ('→', "or[not[%s], %s]"), ('∨', "or[%s, %s]"), ('∧', "and[%s, %s]")]
    if any([symbol[0] in row for symbol in symbols]):
        for symbol, pattern in symbols:
            if symbol in row:
                index = row.index(symbol)
                left = row[:index]
                if '̅' in left:
                    left = f'not[{left[:-1]}]'
                right = row[index + 1:]
                if '̅' in right:
                    right = f'not[{right[0:-1]}]'
                return pattern % (left, right)
    return 'not[' + row[:-1] + ']'


def get_vars(row: str):
    """
    Get vars from translated to python string.
    """
    row = row.replace('xor', '').replace('and', '').replace('or', '').replace('not', '').replace('(', '') \
        .replace(')', '').replace(',', '').replace(' ', '')
    return sorted(list(set(row)))


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.knf = ''
        self.cnf = ''
        self.variables = None
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
        """
        Handles user input from ui keyboard.
        """
        btn = self.sender()

        allowed_buttons = ('btn_brace_left', 'btn_brace_right', 'btn_arr_down', 'btn_arr_right', 'btn_x',
                           'btn_y', 'btn_z', 'btn_a', 'btn_b', 'btn_d', 'btn_c', 'btn_eq', 'btn_sheff',
                           'btn_or_2', 'btn_or', 'btn_xor')

        if btn.objectName() in allowed_buttons:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text().upper())

    def calculate(self) -> None:
        """
        Logic performed, when user hits 'calculate' button.
        """
        self.cnf = ''
        self.knf = ''
        value = self.ui.lineEdit.text()
        value = '(' + value + ')'
        human_result = translate_to_python(value).replace('[', '(').replace(']', ')')

        self.variables = get_vars(human_result)

        # Replace canonical discrete math names to in-code ones.
        result = human_result.replace('xor', 'temp').replace('and', 'and_logic').replace('or', 'or_logic') \
                             .replace('not', 'not_logic').replace('temp', 'xor_logic')

        logger.debug(f"Entered vars: {self.variables}")

        table = PrettyTable()
        table.field_names = self.variables + ['F']

        for values in zip(*get_combinations(len(self.variables))):
            tmp_result = result
            for var, val in zip(self.variables, values):
                tmp_result = tmp_result.replace(var, str(val))
            ans = eval(tmp_result)
            # Convert to list to add to the table
            values = list(values)
            table.add_row(values + [int(ans)])
            if int(ans) == 1:
                self.get_cnf(values)
            else:
                self.get_knf(values)

        output_pattern = f"""Введённое выражение: 
{human_result}
        
Таблица истинности: 
{table}

СДНФ:
{self.cnf[:-1]}

СКНФ:
{self.knf[:-1]}
"""

        self.ui.lineEdit_2.setText(output_pattern)

        logger.debug('\n' + str(table))
        logger.debug('SCNF: ' + self.cnf + '\n')
        logger.debug('SKNF: ' + self.knf + '\n')

    def clear_all(self) -> None:
        """
        Clears all user input.
        """
        self.entry.setText('')

    def backspace(self) -> None:
        """
        Clears last symbol.
        """
        entry = self.entry.text()

        if len(entry) == 0:
            return

        self.entry.setText(entry[:-1])

    def get_cnf(self, values):
        result = ''
        for var, value in zip(self.variables, values):
            if value == 0:
                result += var + '̅'
            else:
                result += var
        self.cnf += result + '∨'

    def get_knf(self, values):
        result = ''
        for var, value in zip(self.variables, values):
            if value == 1:
                result += var + '̅' + '∨'
            else:
                result += var + '∨'
        result = result[:-1]
        self.knf += '(' + result + ')' + '∧'


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
