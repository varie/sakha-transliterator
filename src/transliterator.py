sakha_dict = {
    'А': 'A', 'а': 'a', 'Ә': 'Ē', 'ә': 'ē', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g', 'Ҕ': 'Ğ', 'ҕ': 'ğ', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'İ', 'и': 'i',
    'Й': 'İ', 'й': 'i', 'К': 'K', 'к': 'k', 'Ҥ': 'Ŋ', 'ҥ': 'ŋ', 'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'Ң': 'Ŋ', 'ң': 'ŋ', 'О': 'O', 'о': 'o',
    'Ө': 'Ӧ', 'ө': 'ӧ', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ү': 'Ү', 'ү': 'ү', 'Ф': 'F', 'ф': 'f',
    'Х': 'H', 'х': 'h', 'Һ': 'H', 'һ': 'h', 'Ц': 'C', 'ц': 'c', 'Ч': 'Ç', 'ч': 'ç',
    'Ш': 'Ş', 'ш': 'ş', 'Щ': 'Ş', 'щ': 'ş', 'Ъ': '', 'ъ': '', 'Ы': 'Y', 'ы': 'y',
    'Ь': '', 'ь': '', 'Э': 'E', 'э': 'e', 'Ю': 'Y', 'ю': 'y', 'Я': 'Ya', 'я': 'ya'
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

def transliterate_sakha(text, mapping):
    """
    Transliterates the given text from Cyrillic Sakha to Novgorodov Sakha using the provided mapping dictionary.

    Parameters:
    - text (str): The text in Cyrillic Sakha script to be transliterated.
    - mapping (dict): A dictionary where the key is Cyrillic Sakha character and the value is the corresponding Novgorodov Sakha character.

    Returns:
    - str: The transliterated text in Novgorodov Sakha script.
    """
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

