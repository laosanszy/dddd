import  allure
@allure.feature("sf")
class Test_py2:
    @allure.story("1")
    def test_demo(self):
        a = 1
        b = 1
        assert a == b

    @allure.story("2")
    def test_demo1(self):
        a = 1
        b = 1
        assert a != b