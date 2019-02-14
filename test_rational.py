from unittest import TestCase
from Rational import Rational


class TestRational(TestCase):

    def test_init_zeroDenominator(self):
        a = 3
        b = 0

        r1 = Rational(a,b)

        self.assertRaises(Exception)

    def test_init_negDenominator(self):
        a = 3
        b = -1

        r1 = Rational(a,b)

        self.assertRaises(Exception)

    def test_init_float(self):
        a = 1.0
        b = 3

        r1 = Rational(a, b)

        self.assertRaises(Exception)

    def test_init_str(self):
        a = "STRING"
        b = 3

        r1 = Rational(a, b)

        self.assertRaises(Exception)

    def test_init_list(self):
        a = [2,1,4]
        b = 3

        r1 = Rational(a, b)

        self.assertRaises(Exception)

    def test_add_common_denominator(self):
        a = 3
        b = 5
        c = 1

        r1 = Rational(a, b)
        r2 = Rational(c, b)

        sum = r1 + r2

        self.assertEqual(sum, Rational(4,5))

    def test_add_different_denominators(self):
        a = 3
        b = 5
        c = 1
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(17,20))

    def test_add_one_negative(self):
        a = -3
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(3,20))

    def test_add_both_negative(self):
        a = -3
        b = 5
        c = -3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(-27,20))

    def test_add_improper_fraction(self):
        a = 14
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 + r2

        self.assertEqual(sum, Rational(71,20))

    def test_add_not_Rationals(self):
        a = 14
        b = 5

        r1 = Rational(a, b)
        r2 = 3

        sum = r1 + r2

        self.assertRaises(Exception)

    def test_sub_common_denominator(self):
        a = 3
        b = 5
        c = 1

        r1 = Rational(a, b)
        r2 = Rational(c, b)

        sum = r1 - r2
        self.assertEqual(sum, Rational(2,5))

    def test_sub_different_denominators(self):
        a = 3
        b = 5
        c = 1
        d = 4

        r1 = Rational(a, b)
        r2 = Rational(c, d)

        sum = r1 - r2

        self.assertEqual(sum, Rational(2,5))

    def test_sub_one_negative(self):
        a = -3
        b = 5
        c = 1
        d = 4

        r1 = Rational(a, b) #-3/5
        r2 = Rational(c, d) # 1/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(-17,20))

    def test_sub_both_negative(self):
        a = -3
        b = 5
        c = -3
        d = 4

        r1 = Rational(a, b) # -3/5
        r2 = Rational(c, d) # -3/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(3,20))

    def test_sub_improper_fraction(self):
        a = 14
        b = 5
        c = 3
        d = 4

        r1 = Rational(a, b) # 14/5
        r2 = Rational(c, d) # 3/4

        sum = r1 - r2

        self.assertEqual(sum, Rational(41,20))

    def test_sub_not_Rationals(self):
        a = 14
        b = 5

        r1 = Rational(a, b)
        r2 = 3

        sum = r1 - r2

        self.assertRaises(Exception)

    def test_str(self):
        a = 5
        b = 7

        r1 = Rational(a, b)

        rationalAsString = str(r1)

        self.assertEqual(rationalAsString, "5/7")

    def test_str_negative(self):
        a = -5
        b = 7

        r1 = Rational(a, b)

        rationalAsString = str(r1)

        self.assertEqual(rationalAsString, "-5/7")

    def test_float_less_than_one(self):
        a = 1
        b = 2

        r1 = Rational(a, b)

        rationalAsFloat = float(r1)

        self.assertEqual(rationalAsFloat, 0.5)

    def test_float_greater_than_one(self):
        a = 3
        b = 2

        r1 = Rational(a, b)

        rationalAsFloat = float(r1)

        self.assertEqual(rationalAsFloat, 1.5)

    def test_float_(self):
        a = 3
        b = 2

        r1 = Rational(a, b)

        rationalAsFloat = float(r1)

        self.assertEqual(rationalAsFloat, 1.5)
