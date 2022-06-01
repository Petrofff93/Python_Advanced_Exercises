def concatenate(*args, **kwargs):
    text = ''

    for item in args:
        text += item

    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))