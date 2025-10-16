def get_num_words( text ):
    return len(text.split())

def get_char_count( text ):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_char_count( char_count ):
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)