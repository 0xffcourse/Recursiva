def tokenize(statement):
    tokens, i, j = [], 0, 0
    while i < len(statement):
        token = statement[i]
        if token in '0123456789.':
            j = 1
            while i+j < len(statement)and statement[i+j]in '0123456789.':
                token += statement[i+j]
                j += 1
            i += j
            tokens += [token]
        elif token == '"':
            j = 1
            token = ''
            while i+j < len(statement)and statement[i+j] != '"':
                token += statement[i+j]
                j += 1
            i += j+1
            tokens += ['"'+token+'"']
        elif token == "'":
            j = 1
            token = ''
            while i+j < len(statement)and statement[i+j] != "'":
                token += statement[i+j]
                j += 1
            i += j+1
            tokens += ["'"+token+"'"]
        elif token == '[':
            j = 1
            token = ''
            while i+j < len(statement)and statement[i+j] != ']':
                token += statement[i+j]
                j += 1
            i += j+1
            tokens += ['['+token+']']
        elif token == ' 'or token == '	':
            i += 1
        elif token == '-':
            j = 1
            while i+j < len(statement)and statement[i+j]in '0123456789.':
                token += statement[i+j]
                j += 1
            i += j
            tokens += [token]
        else:
            i += 1
            tokens += [token]
    return tokens
