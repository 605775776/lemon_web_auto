from selenium.webdriver.common.by import By


class AddPageLocs:

    # 学生姓名
    student_name = (By.XPATH, "//input[@placeholder='请填写学生姓名']")
    # 资源类型
    resource_type = (By.XPATH, "//input[@placeholder='请选择资源类型']")

    # 资源类型-校区前台电话
    resource_type_1 = (By.XPATH, "//li/span[text()='校区前台电话']")
    # 资源类型-临访
    resource_type_2 = (By.XPATH, "//li/span[text()='临访']")
    # 资源类型-总部呼入
    resource_type_3 = (By.XPATH, "//li/span[text()='总部呼入']")
    # 资源类型-总部其他资源
    resource_type_4 = (By.XPATH, "//li/span[text()='总部其他资源']")
    # 资源类型-学管师挖掘/转介绍
    resource_type_5 = (By.XPATH, "//li/span[text()='学管师挖掘/转介绍']")
    # 资源类型-课程顾问/咨询师挖掘资源
    resource_type_6 = (By.XPATH, "//li/span[text()='课程顾问/咨询师挖掘资源']")

    # 来源渠道
    source_channel = (By.XPATH, "//input[@placeholder='请选择来源渠道']")

    # 来源渠道-外呼中心
    source_channel_1 = (By.XPATH, "//li/span[text()='外呼中心']")
    # 来源渠道-营销短信
    source_channel_2 = (By.XPATH, "//li/span[text()='营销短信']")
    # 来源渠道-官网/微信
    source_channel_3 = (By.XPATH, "//li/span[text()='官网/微信']")
    # 来源渠道-宣传单
    source_channel_4 = (By.XPATH, "//li/span[text()='宣传单']")
    # 来源渠道-户外广告
    source_channel_5 = (By.XPATH, "//li/span[text()='户外广告']")
    # 来源渠道-在读
    source_channel_6 = (By.XPATH, "//li/span[text()='在读']")
    # 来源渠道-亲朋好友
    source_channel_7 = (By.XPATH, "//li/span[text()='亲朋好友']")
    # 来源渠道-114查询
    source_channel_8 = (By.XPATH, "//li/span[text()='114查询']")
    # 来源渠道-老学员介绍
    source_channel_9 = (By.XPATH, "//li/span[text()='老学员介绍']")
    # 来源渠道-沉睡/结课
    source_channel_10 = (By.XPATH, "//li/span[text()='沉睡/结课']")
    # 来源渠道-报媒广告
    source_channel_11 = (By.XPATH, "//li/span[text()='报媒广告']")
    # 来源渠道-其他业务线推荐
    source_channel_12 = (By.XPATH, "//li/span[text()='其他业务线推荐']")

    # 资源日期
    collect_date = (By.XPATH, "//input[@placeholder='选择日期时间']")

    # 资源日期为今天
    collect_date_today = (By.XPATH, "//button[text()='今天']")

    # 资源日期为昨天
    collect_date_yesterday = (By.XPATH, "//button[text()='昨天']")

    # 资源日期为一周前
    collect_date_last_week = (By.XPATH, "//button[text()='一周前']")

    # 资源质量
    resource_stars = (By.XPATH, "//span[@class='el-rate__item'][5]")
    # 资源进展
    resource_progress = (By.XPATH, "//input[@placeholder='请选择资源进展']")

    # 首次上门日期
    first_visit_date = (By.XPATH, "(//input[@placeholder='选择日期'])[1]")
    # 最迟回访日期
    late_visit_date = (By.XPATH, "(//input[@placeholder='选择日期'])[2]")
    # 年级
    collect_grade = (By.XPATH, "//input[@placeholder='请选择年级']")
    # 班级
    resource_class = (By.XPATH, "//input[@placeholder='请填写班级,如五班']")
    # 就读学校
    school = (By.XPATH, "//input[@placeholder='请输入学校名称搜索']")
    # 资源描述
    resource_desc = (By.XPATH, "//textarea[@placeholder='请填写资源描述,8~800中文字']")
    # 联系人关系
    contact_relationship = (By.XPATH, "(//input[@placeholder='请选择'])[1]")
    # 联系人姓名
    contact_name = (By.XPATH, "//input[@placeholder='请输入联系人姓名']")
    # 联系人手机/固话
    contact_phone = (By.XPATH, "//input[@placeholder='请输入联系手机/固话']")
    # 备注
    contact_remark = (By.XPATH, "//input[@placeholder='请输入备注']")
    # 性别
    resource_sex = (By.XPATH, "//span[@class='el-radio__label']")
    # 生日
    resource_birthday = (By.XPATH, "(//input[@placeholder='选择日期'])[3]")
    # 推荐老师
    recommend_teacher = (By.XPATH, "//input[@placeholder='请输入老师姓名搜索']")
    # 科目
    intention_subject = (By.XPATH, "//input[@placeholder='请选择科目']")
    # 地址/校区
    resource_address = (By.XPATH, "//input[@placeholder='请填写地址/小区']")

    # 确认添加
    confirm_add = (By.XPATH, "//button/span[text()='确认添加']")
