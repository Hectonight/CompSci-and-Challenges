def generate_hashtag(txt):
    final = '#' + txt.title().replace(' ', '').replace('    ', '')
    final = False if ((len(final) > 140) or ('#' == final)) else final
    return final


print(generate_hashtag('BOBEROOO'))