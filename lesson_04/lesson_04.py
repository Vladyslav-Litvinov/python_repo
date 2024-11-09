adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# task 02 ==
""" Замініть .... на пробіл
"""

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

# task 01
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03
import re
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
h_count = adwentures_of_tom_sawer.count('h')
print(h_count)

# task 05
capitalized_words_count = sum(1 for word in adwentures_of_tom_sawer.split() if word[0].isupper())
print(capitalized_words_count)

# task 06
second_tom_position = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)
print(second_tom_position)

# task 07
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?]) +', adwentures_of_tom_sawer)

# task 08
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
by_the_time_exists = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print(by_the_time_exists)

# task 10
last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print(last_sentence_word_count)