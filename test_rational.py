from unittest import TestCase
from Rational import Rational

class TestRational(TestCase):

    def add_common_denominator(self):
        a = 3
        b = 5
        c = 1


        r1 = Rational(a, b)
        r2 = Rational(c, b)

        sum = r1 + r2

        self.assertEqual(sum, Rational(4,5))

    def add_different_denominators(self):

        a = 3
        b = 5
        c = 1
        d = 4


        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(17,20))

    def add_one_negative(self):

        a = -3
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(3,20))


    def add_both_negative(self):

        a = -3
        b = 5
        c = -3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(-27,20))

    def add_improper_fraction(self):
        a = 14
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(71,20))

    def add_not_Rationals(self):
        a = 14
        b = 5

        r1 = Rational(a, b)
        r2 = 3

        sum = r1 + r2

        self.assertRaises(Exception)

    def sub_common_denominator(self):
        a = 3
        b = 5
        c = 1

        r1 = Rational(a, b)
        r2 = Rational(c, b)

        sum = r1 - r2
        self.assertEqual(sum, Rational(2,5))

    def sub_different_denominators(self):

        a = 3
        b = 5
        c = 1
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 - r2

        self.assertEqual(sum, Rational(2,5))

    def sub_one_negative(self):

        a = -3
        b = 5
        c = 1
        d = 4

        r1 = Rational(a, b) #-3/5
        r2 = Rational(c, d) # 1/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(-17,20))

    def sub_both_negative(self):

        a = -3
        b = 5
        c = -3
        d = 4

        r1 = Rational(a, b) # -3/5
        r2 = Rational(c, d) # -3/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(3,20))

    def sub_improper_fraction(self):
        a = 14
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b) # 14/5
        r2 = Rational(c, d) # 3/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(41,20))

    def sub_not_Rationals(self):
        a = 14
        b = 5

        r1 = Rational(a, b)
        r2 = 3

        sum = r1 - r2

        self.assertRaises(Exception)