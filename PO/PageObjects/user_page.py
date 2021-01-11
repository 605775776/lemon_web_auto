from PO.PageLocators.index_page_locs import IndexPageLocs as loc
from PO.PageLocators.user_page_locs import UserPageLocs as loc
from PO.Common.basepage import BasePage


class UserPage(BasePage):

    # 获取用户余额
    def get_user_money(self):
        return self.get_ele_text(loc.user_leftMoney, "用户页面-获取余额").strip("元")