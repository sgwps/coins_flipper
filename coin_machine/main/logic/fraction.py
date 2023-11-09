def GCF(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def isint(other):
    if isinstance(other, int):
        other = Fraction(other)
    return other


class Fraction:

    def __init__(self, num = 0, denom = 1):
        divid = GCF(abs(num), abs(denom))
        self.numer = abs(num) // divid
        self.denom = abs(denom) // divid
        if num * denom < 0:
            self.numer *= -1


    def decimal(self):
        return str(self.numer / self.denom, 4)

    def __str__(self):
        if self.denom != 1:
            return str(self.numer) + '/' + str(self.denom)
        else:
            return str(self.numer)

    def __lt__(self, other):
        if (self - other).numer < 0:
            return True
        else:
            return False

    def __le__(self, other):
        if (self - other).numer <= 0:
            return True
        else:
            return False

    def __eq__(self, other):
        if (self - other).numer == 0:
            return True
        else:
            return False

    def __ne__(self, other):
        if (self - other).numer != 0:
            return True
        else:
            return False

    def __gt__(self, other):
        if (self - other).numer > 0:
            return True
        else:
            return False

    def __ge__(self, other):
        if (self - other).numer >= 0:
            return True
        else:
            return False

    def __add__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __radd__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __iadd__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __rsub__(self, other):
        other = isint(other)
        return Fraction(- self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __isub__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __rmul__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __imul__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom, self.denom * other.numer)

    def __rtruediv__(self, other):
        other = isint(other)
        return Fraction(self.denom * other.numer, self.numer * other.denom)

    def __itruediv__(self, other):
        other = isint(other)
        return Fraction(self.numer * other.denom, self.denom * other.numer)

    def __pos__(self):

        return self

    def __neg__(self):

        return Fraction(-self.numer, self.denom)

    def abs(self):
        
        return Fraction(abs(self.numer), self.denom)

    def int_part(self):

        return self.numer // self.denom

    def int_part2(self):

        return abs(self.numer) // self.denom

    def frac_part(self):

        return Fraction(self.numer % self.denom, self.denom)

    def frac_part2(self):

        return Fraction(abs(self.numer) % self.denom, self.denom)

    def inverse(self):

        return Fraction(self.denom, self.numer)

    def max_aliquote(self):
        if self.numer == 1:
            return self
        else:
            i = 1
            j = 10 ** 100
            while j - i > 1:
                mid = (i + j) // 2
                if Fraction(1, mid) < self:
                    j = mid
                else:
                    i = mid
            return Fraction(1, j)

    def egypt_fractions(self):
        a = []
        while self != 0:
            a.append(self.max_aliquote())
            self -= a[-1]
        k = ''
        k += str(a[0])
        for i in a[1:]:
            k += '+'
            k += str(i)
        return k

    @staticmethod
    def from_continued(terms):
        terms[-1] = Fraction(terms[-1])
        for i in range(len(terms) - 1, 0, -1):
            terms[i - 1] += (1 / terms[i])
        return terms[0]

    def to_continued(self):
        a = []
        test = True
        while True:
            a.append(self.int_part())
            self -= a[-1]
            if self == 0:
                return a
            else:
                self = self.inverse()

    def closest(self, den):
        a = (self.numer * den) // self.denom
        if (Fraction(a, den) - self).abs() > (Fraction(a + 1, den) - self).abs():
            return Fraction(a + 1, den)
        else:
            return Fraction(a, den)

    def limit_denominator(self, q):
        b = self.int_part()
        self = self.frac_part()
        if self > self - 1:
            difference = 1 - self
            minn = Fraction(1)
        else:
            difference = self
            minn = Fraction()
        for i in range(2, q + 1):
            a = self.closest(i)
            if (a - self).abs() < difference:
                minn = a
                difference = (a - self).abs()
        return minn + b

    @staticmethod
    def from_repeating(terms):
        if terms[0] == '-':
            i = 1
            k = -1
        else:
            i = 0
            k = 1
        if '(' in terms:
            int_part = ''
            while terms[i] != '.':
                int_part += terms[i]
                i += 1
            if int_part == '':
                int_part = 0
            else:
                int_part = int(int_part)
            i += 1
            frac_part1 = ''
            while terms[i] != '(':
                frac_part1 += terms[i]
                i += 1
            i += 1
            frac_part2 = ''
            while terms[i] != ')':
                frac_part2 += terms[i]
                i += 1
            den = int('9' * len(frac_part2) + '0' * len(frac_part1))
            frac_part2 = int(frac_part1 + frac_part2)
            if frac_part1 == '':
                frac_part1 = 0
            else:
                frac_part1 = int(frac_part1)
            frac_part2 -= frac_part1
            return Fraction(den * int_part + frac_part2, den * k)
        else:
            if '.' in terms:
                int_part = ''
                while terms[i] != '.':
                    int_part += terms[i]
                    i += 1
                if int_part == '':
                    int_part = 0
                else:
                    int_part = int(int_part)
                i += 1
                frac_part = terms[i:]
                den = int('1' + '0' * len(frac_part))
                frac_part = int(frac_part)
                return Fraction(den * int_part + frac_part, den * k)
            else:
                return Fraction(int(terms[i:]), k)

    def to_repeating(self):
        if (self.denom == 1):
            return self
        k = ''
        if (self.numer < 0):
            k = '-'
        int_part = self.int_part2()
        self = self.frac_part2()
        modulo = dict()
        i = True
        count = 0
        result = ''
        while i:
            self.numer *= 10
            result += str(self.numer // self.denom)
            self.numer %= self.denom
            if self.numer in modulo:
                modulo[self.numer] = (modulo[self.numer], count)
                f = self.numer
                i = False
            elif self.numer == 0:
                modulo[self.numer] = 0
                i = False
            else:
                modulo[self.numer] = count
            count += 1
        if 0 in modulo:
            if int(result) == 0:
                return k + str(int_part) 
            else:
                return k + str(int_part) + '.' + result
        elif 0 in modulo[f] and result[0] == result[-1]:
            return k + str(int_part) + '.' + '(' + result[:-1] + ')'
        else:
            frac_part1 = result[:modulo[f][0] + 1]
            frac_part2 = result[modulo[f][0] + 1:]
            result = str(int_part) + '.' + frac_part1 + '(' + frac_part2 + ')'
            return k + result
