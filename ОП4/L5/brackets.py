def brackets(seq):
    chars = '({[<>]})'

    for i in seq:
        if i not in chars:
            seq = seq.replace(i, '')

    while '()' in seq or '[]' in seq or '{}' in seq or '<>' in seq:
        seq = seq.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')

    return seq == ''
