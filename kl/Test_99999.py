import pytest,allure

class T0:
    @pytest.mark.parametrize("a",[1,2,3])
    @allure.step(title="第一步")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.issue("bug位置")
    @allure.testcase("标记用例")
    def Test_555(self,a):
        allure.attach("测试是否相等","pd")
        assert a == 2,"成功"

