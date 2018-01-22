class TestCase:
    def newInstance(user_input,passing=False,output="",expected=""):
        _test_case = dict()
        _test_case['passing'] = passing
        _test_case['input'] = user_input
        _test_case['output'] = output
        _test_case['expected'] = expected
        return _test_case
