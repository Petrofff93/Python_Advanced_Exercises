def words_sorting(*args):
    words_dict = {}
    value = 0

    for word in args:
        for ch in word:
            value += ord(ch)
        words_dict[word] = value
        value = 0

    if sum(words_dict.values()) % 2 == 0:
        result = [f'{key} - {value}' for key, value in sorted(words_dict.items())]
        return '\n'.join(result)
    else:
        result = [f'{key} - {value}' for key, value in sorted(words_dict.items(), key=lambda x: -x[1])]
        return '\n'.join(result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
