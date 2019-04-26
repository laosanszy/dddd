from Common import Request, Assert, Deng, read_excel
import allure
import pytest

sku_bian = 0
request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:8080/'
head = {}
idsList=[]
excel_list = read_excel.read_excel_list('./document/tuihuo.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())




@allure.feature("退货模块")
class Test_tui:
    @allure.story("查看")
    def test_tui(self):
        global head
        head = Deng.Test_cha().test_cha()
        para = {'pageNum': '1', 'pageSize': '5'}
        get_sku_resp = request.get_request(url=url + 'returnReason/list/', params=para, headers=head)
        resp_json = get_sku_resp.json()
        assertion.assert_code(get_sku_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
        json_data = resp_json['data']
        data_list = json_data['list']
        bian = data_list[0]
        global sku_bian
        sku_bian = bian['id']



    @allure.story("删除")
    def test_shan(self):
        del_shan_resp = request.post_request(url=url + 'returnReason/delete/',params={'ids':sku_bian}, headers=head)
        resp_json = del_shan_resp.json()
        assertion.assert_code(del_shan_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story("添加")
    @pytest.mark.parametrize("name,sort,status,msg",excel_list,ids=idsList)
    def test_tian(self,name,sort,status,msg):
        json = {"name": name, "sort": sort, "status": status, "createTime": ""}
        add_resp = request.post_request(url=url+'returnReason/create',json=json,headers=head)
        resp_json = add_resp.json()
        assertion.assert_code(add_resp.status_code,200)
        assertion.assert_in_text(resp_json['message'],msg)










