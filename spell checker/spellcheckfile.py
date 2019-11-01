from spellchecker import SpellChecker

spell = SpellChecker()  
spell.word_frequency.load_text_file('./Geo.txt')


spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
spell.known(['microsoft', 'google'])  
