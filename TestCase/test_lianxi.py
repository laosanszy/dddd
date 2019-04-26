from Common import Request,Assert
import allure

request = Request.Request()
assertion = Assert.Assertions()

url = 'http://192.168.1.137:1811/'

@allure.feature("用户模块")
class Test_lianxi:
    @allure.story("注册测试")
    def test_zhu(self):
        jsons = {"phone": "18825074533","pwd": "hhh789363","rePwd": "hhh789363","userName": "ggg123453"}
        resp_zhu = request.post_request(url=url +'user/signup',json=jsons)
        req_json = resp_zhu.json()
        assertion.assert_code(resp_zhu.status_code, 200)
        assertion.assert_in_text(req_json['respBase'],'成功')

