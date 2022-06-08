def line_modification(line):
    current_result = ' '.join(reversed(line.strip().split()))
    return current_result


punctuation_set = {"-", ",", ".", "!", "?"}

with open('text.txt', 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            new_text = line_modification(line)
            for punc in punctuation_set:
                if punc in new_text:
                    new_text = new_text.replace(punc, '@')
            print(new_text)

