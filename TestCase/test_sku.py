from Common import Request, Assert, read_excel
import allure
import pytest
sku_bian = 0
request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:8080/'
head = {}
@allure.feature("商品模块")
class Test_sku:
    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url + 'admin/login',
                                          json={"username": "admin", "password": "123456"})

        resp_text = login_resp.text
        print(type(resp_text))

        resp_dict = login_resp.json()

        print(type(resp_dict))

        assertion.assert_code(login_resp.status_code, 200)

        assertion.assert_in_text(resp_dict['message'], '成功')
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHend = data_dict['tokenHead']
        global head
        head = {'Authorization': tokenHend + token}

    @allure.story("获取商品分类")
    def test_get_sku(self):
        para = {'pageNum':'1','pageSize':'10'}
        get_sku_resp = request.get_request(url=url +'productCategory/list/0',params = para,headers = head)
        resp_json = get_sku_resp.json()
        assertion.assert_code(get_sku_resp.status_code,200)
        assertion.assert_in_text(resp_json['message'],'成功')


        json_data = resp_json['data']
        data_list = json_data['list']
        bian = data_list[0]
        global sku_bian
        sku_bian = bian['id']

    @allure.story("删除商品分类")
    def test_get_sku2(self):
        del_sku_resp = request.post_request(url=url +'productCategory/delete/'+str(sku_bian),headers=head)
        resp_json = del_sku_resp.json()
        assertion.assert_code(del_sku_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story("添加商品分类")
    def test_get_sku3(self):
        rep_json = {"description": "", "icon": "", "keywords": "", "name": "hkjsdhkjsd", "navStatus": 0, "parentId": 0}
        del_sku_resp = request.post_request(url=url +'productCategory/create',json=rep_json,headers=head)
        rep_json = del_sku_resp.json()
        assertion.assert_code(del_sku_resp.status_code, 200)

        assertion.assert_in_text(rep_json['message'], '成功')

    @allure.story("数据化商品分类")
    @pytest.mark.parametrize('name',['test1','test2','test3'],ids=['第一个','第二个','第三个'])
    def test_get_sku4(self,name):
        rep_json = {"description": "", "icon": "", "keywords": "", "name": name, "navStatus": 0, "parentId": 0}
        del_sku_resp = request.post_request(url=url + 'productCategory/create', json=rep_json, headers=head)
        rep_json = del_sku_resp.json()
        assertion.assert_code(del_sku_resp.status_code, 200)

        assertion.assert_in_text(rep_json['message'], '成功')
