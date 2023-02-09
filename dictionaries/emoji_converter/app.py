def emoji_converter(message):
    message = input('>')
    words = message.split(' ')

    emojis = {
        ':)': '😄',
        ':(': '😔'
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '

    return output


print(emoji_converter('Good morning! :)'))
