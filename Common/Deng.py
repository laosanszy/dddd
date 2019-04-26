from Common import Request,Assert
import allure

request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:8080/'
class Test_cha:

    def test_cha(self):
        cha_resp=request.post_request(url=url + 'admin/login',
                             json={"username": "admin", "password": "123456"})
        resp_text = cha_resp.text
        print(type(resp_text))
        resp_dict = cha_resp.json()
        assertion.assert_code(cha_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')
        assertion.assert_in_text(resp_dict['message'], '成功')
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHend = data_dict['tokenHead']
        head = {'Authorization': tokenHend + token}
        return head
