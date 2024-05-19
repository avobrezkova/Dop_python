# Алгоритм Рабина-Карпа

def rabin_karp(text, pattern):
    d = 256  # Размер алфавита (ASCII символов)
    q = 101  # Простое число
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0  # Хеш для подстроки
    t = 0  # Хеш для текста

    # Вычисление хеша для подстроки и первой подстроки текста
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Поиск вхождений
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if pattern[j] != text[i+j]:
                    match = False
                    break
            if match:
                print("Найдено вхождение подстроки на позиции", i)

        if i < n - m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t = t + q

text = "Буря мглою небо кроет. Вихри снежные крутя. То как зверь она завоет, то заплачет как дитя"
pattern = "рое"
rabin_karp(text, pattern)

# Алгоритм на основе конечного автомата.

NO_OF_CHARS = 256

def NextState(pois, A, state, x):
    if state < A and x == ord(pois[state]):
        return state+1

    i = 0
    for k in range(state,0,-1):
        if ord(pois[k-1]) == x:
            while i<k-1:
                if pois[i] != pois[state-k+1+i]:
                    break
                i += 1
            if i == k-1:
                return k
    return 0

def compTF(pois, A, TF):
    for state in range(A+1):
        for x in range(NO_OF_CHARS):
            TF[state][x] = NextState(pois, A, state, x)

def finit_automat(pois, text):
    A = len(pois)
    B = len(text)
    TF = [[0]*NO_OF_CHARS for _ in range(A+1)]

    compTF(pois, A, TF)

    state = 0
    for i in range(B):
        state = TF[state][ord(text[i])]
        if state == A:
            print("Найдено вхождение подстроки на позиции", i-A+1)

text = "ARTARTARTARTARTARTISTARTARTARTART"
pois = "ARTI"
finit_automat(pois, text)