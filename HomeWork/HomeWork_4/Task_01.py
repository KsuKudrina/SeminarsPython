
# Вычислить число Пи c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = float(input('Введите число: '))
def calc_pi(eps=1.0e-5):
    s = 0
    n = 1
    sgn = 1
    while True:
        a = 4/n
        s = s + sgn *a
        if a < eps:
            return s
        sgn = -sgn
        n = n + 2
pi = calc_pi()
print(pi)

d = str(d)
d = d.split('.')
d = len(d[1])
print(round(pi, d))
