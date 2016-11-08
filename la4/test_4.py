#!/usr/bin/env python3
"""
Unit testing for lab 4 built on the unittest module.

Note:
If you have downloaded the scripts from the website it might not
have the access right. To solve this run:
$ chmod +x <path_to_test_4.py>

Usage (case insensitive for parameters to --test):
$ ./test_4.py --test a <path_to_lab>
to test lab 4A
$ ./test_4.py --test b <path_to_lab>
to test lab 4B
$ ./test_4.py --test c <path_to_lab>
to test lab 4C
$ ./test_4.py --test d <path_to_lab>
to test lab 4D
$ ./test_4.py <path_to_lab>
to test whole lab 4

Initial version by Erik Hansson <erik.b.hansson@liu.se>

Changelog:
 * 31/8-2016: Updated the printed traceback in case that the given file
   can not be imported.
"""


from argparse import ArgumentParser
from importlib.machinery import SourceFileLoader
import sys
from traceback import format_exc
from copy import copy
from unittest import TestCase, defaultTestLoader, TextTestRunner
from math import sin


def deep_sorted(_item: list) -> list:
    """
    Sorts _item in a recursive manner
    """
    item = copy(_item)
    for i in range(len(item)):
        if isinstance(item[i], list):
            item[i] = deep_sorted(item[i])
    return sorted(item)


class TestPowerset(TestCase):
    """
    A Unittest that tests the powerset function
    """

    def testEmpty(self):
        self.assertEqual(lab4.powerset([]), [[]])

    def testLenthOne(self):
        self.assertEqual(deep_sorted(lab4.powerset([1])),
                         deep_sorted([[], [1]]))

    def testStrings(self):
        self.assertEqual(deep_sorted(lab4.powerset(["ridcully","librarian"])),
                         deep_sorted([[], ['ridcully'], ['librarian'],
                                      ['ridcully', 'librarian']]))

    def testInteger(self):
        self.assertEqual(deep_sorted(lab4.powerset([1,2,3])),
                         deep_sorted([[], [1], [2], [3], [1,2],
                                      [1,3], [2,3], [1,2,3]]))


class TestGenerateHeight(TestCase):
    """
    Tests all the generate height funcition
    """

    def setUp(self):
        self._generated_functions = (
            lab4.generate_height(0, 0, 0, 290),
            lab4.generate_height(20, 10, 0, 30),
            lab4.generate_height(0.5, 1, 2, 0.1),
            lab4.generate_height(42, 0, 0, 0)
        )
        self._args = (5, 1, 0, 42)
        self._expected_res = (3625, 45, -1.3, 42)

    def testIsAnonymous(self):
        """
        Tests so that all the generated functions are of the correct type
        """
        for fn in self._generated_functions:
            self.assertIsInstance(fn, type(lambda:0))
            self.assertEqual(fn.__name__, (lambda:0).__name__)

    def testAnswer(self):
        """
        Tests so that the answers are correct
        """
        for fn, arg, res in \
            zip(self._generated_functions, self._args, self._expected_res):
            self.assertEqual(fn(arg), res)


class TestSmoothing(TestCase):
    """
    Unit tests for the smoothing functions
    """

    _allowed_diff = 0.0001

    def testSmooth(self):
        """
        Tests the smooth function
        """
        self.assertTrue(abs(lab4.smooth(lambda x: x**2)(10)-100.000000666666) <
                        self._allowed_diff)
        self.assertTrue(abs(lab4.smooth(lambda x: x**3)(10)-1000.00002000001) <
                        self._allowed_diff)
        self.assertTrue(abs(lab4.smooth(sin)(0.456)-0.44036035495318304) <
                        self._allowed_diff)
        self.assertTrue(abs(lab4.smooth(lambda x:x**0.5)(9)-2.99999999691358) <
                        self._allowed_diff)

    def testTwiceSmoothedSquare(self):
        """
        Tests the twice smoothed square function
        """
        self.assertTrue(abs(lab4.twice_smoothed_square(10)-100.00000133333333) <
                        self._allowed_diff)
        self.assertNotEqual(lab4.twice_smoothed_square(10),
                            lab4.smooth(lambda x:x)(10))
        self.assertTrue(abs(lab4.twice_smoothed_square(0)-0) <
                        self._allowed_diff)
        self.assertTrue(abs(lab4.twice_smoothed_square(-2))-4.000001333333333 <
                        self._allowed_diff)
        self.assertNotEqual(lab4.twice_smoothed_square(-2),
                            lab4.smooth(lambda x:x)(-2))

    def testTwiceSmoothedSin(self):
        """
        Tests the twice smoothed sin function
        """
        self.assertTrue(abs(lab4.twice_smoothed_sin(0.456)-0.440359621019886) <
                        self._allowed_diff)
        self.assertNotEqual(lab4.twice_smoothed_sin(0.456),
                            lab4.smooth(sin)(0.456))
        self.assertTrue(abs(lab4.twice_smoothed_sin(0.1)-0.09983335009123369) <
                        self._allowed_diff)
        self.assertNotEqual(lab4.twice_smoothed_sin(0.1),
                            lab4.smooth(sin)(0.1))
        self.assertTrue(abs(lab4.twice_smoothed_sin(-1)+0.8414704238273801) <
                        self._allowed_diff)
        self.assertNotEqual(lab4.twice_smoothed_sin(-1),
                            lab4.smooth(sin)(-1))
        self.assertTrue(abs(lab4.twice_smoothed_sin(0)) < self._allowed_diff)

    def testRepeatedlySmoothed(self):
        """
        Tests the repeatedly smoothed function
        """
        self.assertTrue(
            abs(lab4.repeatedly_smoothed(lambda x: x**2, 5)(10)-
                100.00000333333332) < self._allowed_diff
        )
        self.assertNotEqual(lab4.repeatedly_smoothed(lambda x: x**2, 5)(10),
                            lab4.twice_smoothed_square(10))
        self.assertTrue(
            abs(lab4.repeatedly_smoothed(sin, 5)(0.456)-0.4403596210198086) <
            self._allowed_diff
        )
        self.assertNotEqual(lab4.repeatedly_smoothed(sin, 5)(0.456),
                            lab4.twice_smoothed_sin(0.456))


class TestTree(TestCase):
    """
    Tests the tree functionality
    """

    def testTraverse(self):
        """
        Tests the traverse function
        """
        empty_fn = lambda : []
        leaf_fn = lambda key: [key]
        inner_fn = lambda key, lv, rv: lv + [key] + rv
        self.assertEqual(
            sorted(lab4.traverse([1, 2, 3], inner_fn, leaf_fn, empty_fn)),
            [1,2,3]
        )
        self.assertEqual(lab4.traverse([], inner_fn, leaf_fn, empty_fn), [])
        self.assertEqual(
            sorted(lab4.traverse([[], 2, [1, 3, [4, 5, 6]]], inner_fn, leaf_fn,
                            empty_fn)),
            [1, 2, 3, 4, 5, 6]
        )

    def testContainsKey(self):
        """
        Tests the contains key function
        """
        self.assertTrue(lab4.contains_key(6, [6, 7, 8]))
        self.assertTrue(lab4.contains_key(2, [6, 7, [[2, 3, 4], 0, []]]))
        self.assertFalse(lab4.contains_key(2, [[], 1, 5]))
        self.assertTrue(lab4.contains_key(1, [[0, 1, []], 3, 4]))
        self.assertFalse(lab4.contains_key("3", [1, 2, 3]))
        self.assertFalse(lab4.contains_key(1, []))

    def testTreeSize(self):
        """
        Tests the tree size function
        """
        self.assertEqual(lab4.tree_size([2, 7, []]), 2)
        self.assertEqual(lab4.tree_size([]), 0)
        self.assertEqual(lab4.tree_size([[1, 2, []], 4, [[], 5, 6]]), 5)

    def testTreeDepth(self):
        """
        Tests the tree depth function
        """
        self.assertEqual(lab4.tree_depth(9), 1)
        self.assertEqual(lab4.tree_depth([]), 0)
        self.assertEqual(lab4.tree_depth([[], 0, 1]), 2)
        self.assertEqual(lab4.tree_depth([1, 5, [10, 7, 14]]), 3)
        self.assertEqual(lab4.tree_depth([[[], 2, []], 0, 2]), 2)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--test",
                            choices = ["a", "A", "b", "B", "c", "C", "d", "D"],
                            default="", required=False)
    arg_parser.add_argument("file")
    args = arg_parser.parse_args()
    if args.file.rfind("/") != -1:
        sys.path.append(args.file[:args.file.rfind("/")])
        potential_name = args.file[args.file.rfind("/")+1:]
    else:
        sys.path.append(".")
        potential_name = args.file
    if potential_name.rfind("."):
        name = potential_name[:potential_name.rfind(".")]
    else:
        name = potential_name
    try:
        lab4 = SourceFileLoader(name, args.file).load_module()
    except:
        print("Could not import lab: " + args.file)
        print("See traceback for further information:")
        print()
        stack_trace = format_exc().split("\n")
        importlib_has_started = False
        importlib_has_ended = False
        for line in stack_trace:
            if not importlib_has_ended and importlib_has_started and \
               line.lstrip().startswith("File") and "importlib" not in line:
                importlib_has_ended = True
            if importlib_has_ended:
                print(line)
            elif not importlib_has_started and \
                 line.lstrip().startswith("File") and "importlib" in line:
                importlib_has_started = True
        exit(1)
    if args.test.upper() == "A":
        res = TextTestRunner(verbosity=2).run(
            defaultTestLoader.loadTestsFromTestCase(TestPowerset)
        ).wasSuccessful()
    elif args.test.upper() == "B":
        res = TextTestRunner(verbosity=2).run(
            defaultTestLoader.loadTestsFromTestCase(TestGenerateHeight)
        ).wasSuccessful()
    elif args.test.upper() == "C":
        res = TextTestRunner(verbosity=2).run(
            defaultTestLoader.loadTestsFromTestCase(TestSmoothing)
        ).wasSuccessful()
    elif args.test.upper() == "D":
        res = TextTestRunner(verbosity=2).run(
            defaultTestLoader.loadTestsFromTestCase(TestTree)
        ).wasSuccessful()
    elif args.test == "":
        suite = defaultTestLoader.loadTestsFromTestCase(TestPowerset)
        suite.addTests(
            defaultTestLoader.loadTestsFromTestCase(TestGenerateHeight)
        )
        suite.addTests(
            defaultTestLoader.loadTestsFromTestCase(TestSmoothing)
        )
        suite.addTests(
            defaultTestLoader.loadTestsFromTestCase(TestTree)
        )
        res = TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    else:
        print("Unknown arguemnt for --test: " + args.test)
        exit(2)
    if res:
        print("The code passed all the tests")
