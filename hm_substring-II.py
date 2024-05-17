# Алгоритм Бойера-Мура

def badHaracter(string, size):
    badHar = [-1]*256
    for i in range(size):
        badHar[ord(string[i])] = i
    return badHar

def BoyerMoore(text, pois):
    a = len(pois)
    b = len(text)
    badHar = badHaracter(pois, a)
    s = 0
    while(s <= b-a):
        j = a-1
        while j >= 0 and pois[j] == text[s+j]:
            j -= 1
        if j < 0:
            print("Найдено вхождение подстроки на позиции", s)
            s += (a-badHar[ord(text[s+a])] if s+a < b else 1)
        else:
            s += max(1, j-badHar[ord(text[s+j])])

text = "ARTARTARTARTARTISTARTARTART"
pois = "ARTI"
BoyerMoore(text, pois)

# Алгоритм Кнута-Морриса-Пратта

def computLPSarray(pois):
    length = 0
    lps = [0] * len(pois)
    i = 1
    while i < len(pois):
        if pois[i] == pois[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def KMP(text, pois):
    A = len(pois)
    B = len(text)
    lps = computLPSarray(pois)

    i = 0
    j = 0
    while i < B:
        if pois[j] == text[i]:
            i += 1
            j += 1

        if j == A:
            print("Найдено вхождение на позиции", i - j)
            j = lps[j - 1]
        elif i < B and pois[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


text = "ABABDABACDABABCABAB"
pois = "ABABCABAB"
KMP(text, pois)