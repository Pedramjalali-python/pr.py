# import string
# from operator import index
# from os.path import split
# from zoneinfo import reset_tzpath
#
# def ZusammenfassendeBereiche():
#     zahlen = [0, 1, 3, 5, 6, 7]
#     neuliste = []  # Einzelne Zahlen
#     ganzliste = []  # Zusammengefasste Bereiche
#
#     anfang = zahlen[0]  # Der Start eines Bereichs
#     for i in range(len(zahlen) - 1):  # Bis zur vorletzten Zahl iterieren
#         if zahlen[i] + 1 != zahlen[i + 1]:  # Prüfen, ob die Sequenz unterbrochen ist
#             if anfang == zahlen[i]:  # Einzelne Zahl
#                 neuliste.append(str(anfang))
#
#             else:
#                 ganzliste.append(f"{anfang}->{zahlen[i]}")
#             anfang = zahlen[i + 1]  # Neuer Bereich beginnt
#
#     ganzliste.append(f"{anfang}->{zahlen[-1]}")
#
#     print("Einzelne Zahlen:", neuliste)
#     print("Zusammengefasste Bereiche:", ganzliste)
#     return neuliste, ganzliste  # Ergebnisse zurückgeben
#
#
# ergebniss = ZusammenfassendeBereiche()
# print("Ergebnisse:", ergebniss)
from operator import index


# [3,4]
# [8,9,10]
#einzeln [1, 6]
# def ZusammenfassendeBereiche():
#     zahlen = [1, 3, 4, 6, 8, 9, 10]
#     einzeln_zahlen = []
#     richtige = []
#
#     anfang = zahlen[0]  # Startwert korrigieren
#     for menge in range(len(zahlen) - 1):
#         if zahlen[menge] + 1 != zahlen[menge + 1]:  # Prüfen, ob der Bereich endet
#             if anfang == zahlen[menge]:  # Einzelzahl
#                 einzeln_zahlen.append(str(anfang))
#             else:  # Bereich
#                 richtige.append(f"{anfang}->{zahlen[menge]}")
#             anfang = zahlen[menge + 1]  # Nächsten Bereich starten
#
#     # Letzten Bereich oder Einzelzahl hinzufügen
#     if anfang == zahlen[-1]:
#         einzeln_zahlen.append(str(anfang))
#     else:
#         richtige.append(f"{anfang}->{zahlen[-1]}")
#
#     print(f"einzeln_zahlen: {einzeln_zahlen}")
#     print(f"richtige: {richtige}")
#     return einzeln_zahlen, richtige
#
#
# ergebnis = ZusammenfassendeBereiche()
# print(ergebnis)
#





#
# def IsomorpheStrings(a, b):
#     # Wenn die Längen unterschiedlich sind, können die Strings nicht isomorph sein
#     if len(a) != len(b):
#         return False  # Unterschiedliche Längen -> nicht isomorph
#
#     # Wörterbücher zum Speichern der Zuordnungen
#     zuordnung_a_b = {}  # Speichert Zuordnung von Zeichen aus `a` zu Zeichen aus `b`
#     zuordnung_b_a = {}  # Speichert Rückzuordnung von Zeichen aus `b` zu Zeichen aus `a`
#
#     # Iteriere durch die Zeichen beider Strings gleichzeitig
#     for i in range(len(a)):
#         char_a = a[i]  # Zeichen aus `a` an Position i
#         char_b = b[i]  # Zeichen aus `b` an Position i
#
#         # Prüfe, ob `char_a` bereits einer Zuordnung folgt
#         if char_a in zuordnung_a_b:
#             # Wenn die Zuordnung nicht mit `char_b` übereinstimmt, sind die Strings nicht isomorph
#             if zuordnung_a_b[char_a] != char_b:
#                 return False
#
#         # Prüfe, ob `char_b` bereits einer Rückzuordnung folgt
#         if char_b in zuordnung_b_a:
#             # Wenn die Rückzuordnung nicht mit `char_a` übereinstimmt, sind die Strings nicht isomorph
#             if zuordnung_b_a[char_b] != char_a:
#                 return False
#
#         # Füge die Zuordnung hinzu
#         zuordnung_a_b[char_a] = char_b  # `char_a` wird zu `char_b` zugeordnet
#         zuordnung_b_a[char_b] = char_a  # `char_b` wird zu `char_a` zurückzugeordnet
#
#     # Wenn keine Konflikte aufgetreten sind, sind die Strings isomorph
#     return True
#
#
# # Testfälle
# print(IsomorpheStrings("autt", "teti"))  # True, da die Zuordnung eindeutig ist
# print(IsomorpheStrings("foo", "bar"))   # False, da 'o' zwei verschiedene Zeichen ('a', 'r') zugeordnet würde
# print(IsomorpheStrings("paper", "title"))  # True, da die Zuordnung eindeutig ist

#
# def word_pattern(pattern, s):
#     """
#     Überprüft, ob ein gegebenes Wortmuster auf einen Satz passt.
#
#     Args:
#         pattern: Ein String aus eindeutigen Buchstaben, der das Muster darstellt.
#         s: Ein Satz, der aus Wörtern besteht.
#
#     Returns:
#         True, wenn das Muster auf den Satz passt, sonst False.
#     """
#
#     words = s.split()  # Teile den Satz in eine Liste von Wörtern auf
#
#     # Überprüfe, ob die Länge des Musters und die Anzahl der Wörter übereinstimmen
#     if len(pattern) != len(words):
#         return False
#
#     # Erstelle zwei Wörterbücher für die Abbildung zwischen Musterschreiben und Wörtern
#     word_to_char = {}  # Map von Wörtern zu Musterschreiben
#     char_to_word = {}  # Map von Musterschreiben zu Wörtern
#
#     # Iteriere über jedes Paar von Musterschreiben und Wort
#     for char, word in zip(pattern, words):
#         # Überprüfe, ob das Musterschreiben bereits einem anderen Wort zugeordnet ist
#         if char in char_to_word and char_to_word[char] != word:
#             return False
#         # Überprüfe, ob das Wort bereits einem anderen Musterschreiben zugeordnet ist
#         if word in word_to_char and word_to_char[word] != char:
#             return False
#         # Füge die Zuordnung zu den Wörterbüchern hinzu
#         word_to_char[word] = char
#         char_to_word[char] = word
#
#     # Wenn alle Prüfungen bestanden sind, passt das Muster
#     return True
#
# # Example usage:
# pattern = "abba"
# s = "dog cat cat dog"
# result = word_pattern(pattern, s)
# print(result)  # Ausgabe: True












#
# def word_pattern():
#     bushtabe = 'abbc'
#     wort = 'ped ram ram ian'
#
#     # Zerlege die Wörter im Satz
#     w = wort.split(' ')
#
#     # Wörterbuch für Zuordnungen
#     worttobuchs = {}
#     buchstoword = {}
#
#     # Überprüfe, ob die Länge von Muster und Satz übereinstimmt
#     if len(bushtabe) != len(w):
#         return False
#
#     # Iteriere über Buchstaben (Muster) und Wörter
#     for buchs, word in zip(bushtabe, w):
#         # Überprüfe Konsistenz der Zuordnung
#         if buchs in buchstoword and buchstoword[buchs] != word:
#             return False
#
#         if word in worttobuchs and worttobuchs[word] != buchs:
#             return False
#
#         # Füge neue Zuordnung hinzu
#         buchstoword[buchs] = word
#         worttobuchs[word] = buchs
#
#     # Falls alle Bedingungen erfüllt sind, passt das Muster
#     return True
#
#
# # Teste die Funktion
# e = word_pattern()
# print(e)  # Erwartete Ausgabe: False


# def Elemententfernen():
#     zahlen = [1, 4, 5, 6, 3]
#     nichtgleich = 0
#     ziel = 4
#
#     # Verwende eine Kopie der Liste, um über die ursprüngliche Liste zu iterieren
#     for zahl in zahlen[:]:  # Erstelle eine Kopie der Liste
#         if zahl == ziel:  # Prüfe, ob das aktuelle Element gleich dem Ziel ist
#             zahlen.remove(zahl)  # Entferne das Ziel-Element
#             return zahlen
#         else:
#             nichtgleich += 1
#
#     return nichtgleich
#
# e = Elemententfernen()
# print(e)


import telebot
import os

bot = telebot.TeleBot('7613198076:AAHBRYyZIs4kY8uC4cBJ2l_p-U9urQCmFWk')

# Verzeichnis, in dem die Musik gespeichert werden soll
music_directory = 'C:\\Users\\Matrix\\Desktop\\music'

# Stelle sicher, dass das Verzeichnis existiert
if not os.path.exists(music_directory):
    os.makedirs(music_directory)


@bot.message_handler(commands=['start'])
def returnn(message):
    bot.send_message(message.chat.id, 'moin pedram')


@bot.message_handler(content_types=['audio'])
def speichern(message):
    # Hole die Audio-Datei
    audio_file = message.audio
    file_info = bot.get_file(audio_file.file_id)

    # Lade die Datei herunter
    downloaded_file = bot.download_file(file_info.file_path)

    # Speichere die Datei
    file_name = os.path.join(music_directory, f"{audio_file.file_id}.ogg")  # oder .mp3, je nach Format
    with open(file_name, 'wb') as f:
        f.write(downloaded_file)

    bot.reply_to(message, 'Die Musik wurde gespeichert.')


bot.polling()












