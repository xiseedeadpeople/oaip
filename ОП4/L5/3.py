def sequence(brackets):
    chars = '({[<>]})'

    for i in brackets:
        if i not in chars:
            brackets = brackets.replace(i, '')

    while '()' in brackets or '[]' in brackets or '{}' in brackets or '<>' in brackets:
        brackets = brackets.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')

    return brackets == ''

if __name__ == "__main__":
    print(sequence('12 / (9) + 2 ()'))
