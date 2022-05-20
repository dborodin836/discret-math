from main import translate_to_python


def test_basic():
    assert translate_to_python('(X⊕Y)') == 'xor[X, Y]'
    assert translate_to_python('(X|Y)') == 'not[and[X, Y]]'
    assert translate_to_python('(X~Y)') == 'not[xor[X, Y]]'
    assert translate_to_python('(X↓Y)') == 'not[or[X, Y]]'
    assert translate_to_python('(X→Y)') == 'or[not[X], Y]'
    assert translate_to_python('(X∨Y)') == 'or[X, Y]'
    assert translate_to_python('(X∧Y)') == 'and[X, Y]'
    assert translate_to_python('(X̅)') == 'not[X]'


if __name__ == '__main__':
    print(translate_to_python('(b̅→(((a̅⊕b)|(c̅↓a))∨(a~b)))'))

