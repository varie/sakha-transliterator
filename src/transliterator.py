import re

sakha_dict = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g',
    'Ҕ': 'Ğ', 'ҕ': 'ğ', 'Д': 'D', 'д': 'd', 'Дь': 'Dj', 'дь': 'dj', 'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'İ', 'и': 'i',
    'Й': 'İ', 'й': 'i', 'К': 'K', 'к': 'k', 'Ҥ': 'Ŋ', 'ҥ': 'ŋ', 'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'Ң': 'Ŋ', 'ң': 'ŋ', 'Нь': 'Nj', 'нь': 'nj',
    'О': 'O', 'о': 'o',
    'Ө': 'Ӧ', 'ө': 'ӧ', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ү': 'Ү', 'ү': 'ү', 'Ф': 'F', 'ф': 'f',
    'Х': 'Q', 'х': 'q', 'Һ': 'H', 'һ': 'h', 'Ц': 'C', 'ц': 'c', 'Ч': 'Ç', 'ч': 'ç',
    'Ш': 'Ş', 'ш': 'ş', 'Щ': 'Ş', 'щ': 'ş', 'Ъ': '', 'ъ': '', 'Ы': 'Y', 'ы': 'y',
    'Ь': '', 'ь': '', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'
}

sakha_dict_Novgorodov_beta = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g', 'Ҕ': 'Ʃ', 'ҕ': 'ʃ', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'İ', 'и': 'i',
    'Й': 'J', 'й': 'j', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'Ң': 'Ŋ', 'ң': 'ŋ', 'О': 'Ɔ', 'о': 'ɔ',
    'Ө': 'Ӧ', 'ө': 'ӧ', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ү': 'Y', 'ү': 'y', 'Ф': 'F', 'ф': 'f',
    'Х': 'Q', 'х': 'q', 'Һ': 'H', 'һ': 'h', 'Ц': 'C', 'ц': 'c', 'Ч': 'Ç', 'ч': 'ç',
    'Ш': 'Ş', 'ш': 'ş', 'Щ': 'Ş', 'щ': 'ş', 'Ъ': '', 'ъ': '', 'Ы': 'ɯ', 'ы': 'ɯ',
    'Ь': '', 'ь': '', 'Э': 'E', 'э': 'e', 'Ю': 'Y', 'ю': 'y', 'Я': 'Ya', 'я': 'ya'
}

multi_symbol_replacements = {
    'Дь': 'Dj', 'дь':'dj', 'Нь': 'Nj', 'нь': 'nj'
}

def transliterate_sakha(text, mapping):
    """
    Transliterates the given text from Cyrillic Sakha to Novgorodov Sakha using the provided mapping dictionary.

    Parameters:
    - text (str): The text in Cyrillic Sakha script to be transliterated.
    - mapping (dict): A dictionary where the key is Cyrillic Sakha character and the value is the corresponding Novgorodov Sakha character.

    Returns:
    - str: The transliterated text in Novgorodov Sakha script.
    """
    regex = re.compile("(%s)" % "|".join(map(re.escape, multi_symbol_replacements.keys())))
    text = regex.sub(lambda mo: multi_symbol_replacements[mo.string[mo.start():mo.end()]], text)
    transliterated_text = ""
    for char in text:
        if char in mapping:
            transliterated_text += mapping[char] if mapping[char] is not None else char
        else:
            transliterated_text += char  # Append the character as is if not found in the mapping

    return transliterated_text


while True:
    text = input("Сахалыы суруй: ")
    transliterated_text = transliterate_sakha(text, sakha_dict)
    print("Transliterated:", transliterated_text)

