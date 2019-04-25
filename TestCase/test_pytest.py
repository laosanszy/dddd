import allure

@allure.feature("gfdg")
class Test_py:
    @allure.story("1")
    def test_demo(self):
        a = 1
        b = 1
        assert a == b

    @allure.story("2")
    def test_demo1(self):
        a = 1
        b = 1
        assert a == b