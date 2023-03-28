
def duplicate_letter_test(sentence_list):
    for word in sentence_list:
        for character in word:
            if word.count(character) > 1:
                return True
    return False


def clean_string(raw_sting):
    punctuation = '.,!'
    clean_list = raw_sting.translate(str.maketrans('', '', punctuation)).split(' ')
    return clean_list


test_string = 'Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The ' \
              'function should return True if the sentence has any word with duplicate letters, else return False. '

test_2 = 'abc defg hij klm nop'

print(duplicate_letter_test(clean_string(test_2)))

