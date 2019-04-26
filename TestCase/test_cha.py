from Common import Request, Assert, read_excel
import allure
import pytest
sku_bian = 0


request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:8080/'
head = {}
idsList=[]
excel_list = read_excel.read_excel_list('./document/youhuijuan.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())



@allure.feature("优惠券模块")
class Test_cha:
    @allure.story("登录")
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
        global head
        head = {'Authorization': tokenHend + token}

    @allure.story("查看测试")
    def test_cha2(self):
        para = {'pageNum': '1', 'pageSize': '10'}
        get_sku_resp = request.get_request(url=url + 'couponHistory/list', params=para, headers=head)
        resp_json = get_sku_resp.json()
        assertion.assert_code(get_sku_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
        json_data = resp_json['data']
        data_list = json_data['list']
        bian = data_list[0]
        global sku_bian
        sku_bian = bian['id']

    @allure.story("删除测试")
    def test_cha3(self):
        del_sku_resp = request.post_request(url=url + 'coupon/delete/' + str(sku_bian), headers=head)
        resp_json = del_sku_resp.json()
        assertion.assert_code(del_sku_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '失败')

    @allure.story('批量添加优惠券')
    @pytest.mark.parametrize("name,amount,minPoint,publishCount,msg",excel_list,ids=idsList)
    def test_cha4(self,name,amount,minPoint,publishCount,msg):
        json = {"type":0,"name":"fgJ","platform":0,"amount":0,"perLimit":1,"minPoint":0,
                "startTime":"2019-04-07T16:00:00.000Z","endTime":"2019-05-06T16:00:00.000Z",
                "useType":0,"note":"","publishCount":0,"productRelationList":[],
                "productCategoryRelationList":[]}
        rep = request.post_request(url=url + 'coupon/create', json=json, headers=head)
        json_rep = rep.json()
        assertion.assert_code(rep.status_code, 200)
        assertion.assert_in_text(json_rep['message'], '成功')



