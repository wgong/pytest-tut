from tut1.myapp.sample import add

"""
to test all
    pytest tut1/tests/test_sample.py
"""


"""
to test a specific function
    pytest tut1/tests/test_sample.py::test_add_num
"""
def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


"""
to test a specific class method:
    pytest tut1/tests/test_sample.py::TestSample::test_add_num1
"""
class TestSample:
    def test_add_num1(self):
        assert add(1, 2) == 3

    def test_add_str1(self):
        assert add("a", "b") == "ab"
