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
        no_of_negative = row.count('̅')
        if no_of_negative == 0:
            return f"xor[{row[index - 1]}, {row[index + 1]}]"
    return row


if __name__ == '__main__':
    print(translate_to_python('((X⊕Y)|(X⊕Y))'))
