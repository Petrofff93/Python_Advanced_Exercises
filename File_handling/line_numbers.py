from string import punctuation


def filter_letter_punc(line):
    punctuation_list = punctuation
    letter_count = 0
    punctuation_count = 0

    for item in line:
        if item in punctuation_list:
            punctuation_count += 1
        if item.isalpha():
            letter_count += 1
    return letter_count, punctuation_count


with open('text.txt', 'r') as input_file:
    with open('output.txt', 'a+') as output_file:
        for idx, line in enumerate(input_file):
            letters_count, punc_count = filter_letter_punc(line)
            output_file.write(f'Line {idx + 1}: {line[0:-1]} ({letters_count})({punc_count})\n')
