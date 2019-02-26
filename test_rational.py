import unittest
from unittest import TestCase
from Rational import Rational


class TestRational(TestCase):

    def test_init_zero_denominator(self):
        num = 3
        den = 0

        Rational(num, den)

        self.assertRaises(ZeroDivisionError)

    def test_init_negative_denominator(self):
        num = 3
        den = -1

        Rational(num, den)

        self.assertRaises(Exception)

    def test_init_float(self):
        num = 1.0
        den = 3

        Rational(num, den)

        self.assertRaises(Exception)

    def test_init_str(self):
        num = "STRING"
        den = 3

        Rational(num, den)

        self.assertRaises(Exception)

    def test_init_list(self):
        num = [2, 1, 4]
        den = 3

        Rational(num, den)

        self.assertRaises(Exception)

    def test_add_common_denominator(self):
        num_1 = 3
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 + rational_2

        expected_num = 4
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_add_different_denominators(self):
        num_1 = 3
        den_1 = 5
        num_2 = 1
        den_2 = 7

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 + rational_2

        expected_num = 26
        expected_den = 35

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_add_one_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 + rational_2

        expected_num = -2
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_add_both_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = -1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 + rational_2

        expected_num = -4
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_add_improper_fraction(self):
        num_1 = 5
        den_1 = 3
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 + rational_2

        expected_num = 28
        expected_den = 15

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_add_non_rational_type_operand(self):
        num = 3
        den = 5

        rational = Rational(num, den)
        non_rational_type = 3

        rational + non_rational_type

        self.assertRaises(Exception)

    def test_sub_common_denominator(self):
        num_1 = 3
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 - rational_2

        expected_num = 2
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_sub_different_denominators(self):
        num_1 = 3
        den_1 = 4
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 - rational_2

        expected_num = 11
        expected_den = 20

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_sub_second_operand_negative(self):
        num_1 = 3
        den_1 = 5
        num_2 = -1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 - rational_2

        expected_num = 4
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_sub_improper_fraction(self):
        num_1 = 7
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 - rational_2

        expected_num = 6
        expected_den = 5

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_sub_non_rational_type_operand(self):
        num = 3
        den = 5

        rational = Rational(num, den)
        non_rational_type = 4

        rational - non_rational_type

        self.assertRaises(Exception)

    def test_mul_both_positive(self):
        num_1 = 3
        den_1 = 7
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 * rational_2

        expected_num = 3
        expected_den = 35

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_multiply_one_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 * rational_2

        expected_num = -3
        expected_den = 25

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_multiply_both_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = -1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 * rational_2

        expected_num = 3
        expected_den = 25

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_mul_improper_fraction(self):
        num_1 = 7
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 * rational_2

        expected_num = 7
        expected_den = 25

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_mul_non_rational_type(self):
        num = 3
        den = 5

        rational = Rational(num, den)
        non_rational_type = 3

        rational * non_rational_type

        self.assertRaises(Exception)

    def test_div_both_positive(self):
        num_1 = 3
        den_1 = 5
        num_2 = 2
        den_2 = 9

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 / rational_2

        expected_num = 27
        expected_den = 10

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_div_first_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = 1
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 / rational_2

        expected_num = -3
        expected_den = 1

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_div_second_negative(self):
        num_1 = 3
        den_1 = 5
        num_2 = -6
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 / rational_2

        expected_num = -1
        expected_den = 2

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_div_both_negative(self):
        num_1 = -3
        den_1 = 5
        num_2 = -2
        den_2 = 5

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 / rational_2

        expected_num = -3
        expected_den = 2

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_div_improper_fraction(self):
        num_1 = 8
        den_1 = 5
        num_2 = 3
        den_2 = 7

        rational_1 = Rational(num_1, den_1)
        rational_2 = Rational(num_2, den_2)

        actual = rational_1 / rational_2

        expected_num = 56
        expected_den = 15

        self.assertEqual(expected_num, actual.n)
        self.assertEqual(expected_den, actual.d)

    def test_div_non_rational_type(self):
        num = 3
        den = 5

        rational = Rational(num, den)
        non_rational_type = 4

        rational / non_rational_type

        self.assertRaises(Exception)

    def test_str_positive(self):
        num = 5
        den = 7

        rational = Rational(num, den)

        rational_as_string = str(rational)

        self.assertEqual(rational_as_string, "5/7")

    def test_str_negative(self):
        num = -5
        den = 7

        rational = Rational(num, den)

        rational_as_string = str(rational)

        self.assertEqual(rational_as_string, "-5/7")

    def test_float_less_than_one(self):
        num = 1
        den = 2

        rational = Rational(num, den)

        rational_as_float = float(rational)

        self.assertEqual(rational_as_float, 0.5)

    def test_float_greater_than_one(self):
        num = 3
        den = 2

        rational = Rational(num, den)

        rational_as_float = float(rational)

        self.assertEqual(rational_as_float, 1.5)

    def test_float_negative(self):
        num = -3
        den = 2

        rational = Rational(num, den)

        rational_as_float = float(rational)

        self.assertEqual(rational_as_float, -1.5)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRational))
runner = unittest.TextTestRunner()
res = runner.run(suite)
print(res)
print("*"*20)
for i in res.failures:
    print(i[1])
