def count_word_occurrences(sentence):
    word_counts = {}  # Создаем пустой словарь для подсчета количества встреч слов

    words = sentence.split()  # Разделяем входную строку на слова
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

        print(word_counts[word], end=' ')  # Выводим количество вхождений текущего слова

    print()  # Перейти на новую строку

# Ввод строки
input_sentence = "во поле береза стояла во поле кудрявая стояла люли-люли стояла люли-люли стояла"

# Вызываем функцию для подсчета количества слов
count_word_occurrences(input_sentence)
