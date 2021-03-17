#coding=gbk
# 添加资源页面元素定位



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
    resource_type_4 = (By.XPATH, "//li/span[text()='总部其它资源']")
    # 资源类型-学管师挖掘/转介绍
    resource_type_5 = (By.XPATH, "//li/span[text()='学管师挖掘/转介绍']")
    # 资源类型-课程顾问/咨询师挖掘资源
    resource_type_6 = (By.XPATH, "//li/span[text()='课程顾问/咨询师挖掘资源']")

    # 来源渠道
    source_channel = (By.XPATH, "//input[@placeholder='请选择来源渠道']")

    # 来源渠道 列表返回的第一个 [last()]
    source_channel_1 = (By.XPATH, "(//body/div)[last()]//li/span")
    # 来源渠道-列表返回的第二个
    source_channel_2 = (By.XPATH, "((//body/div)[last()]//li/span)[2]")
    # 来源渠道-列表返回的第三个
    source_channel_3 = (By.XPATH, "((//body/div)[last()]//li/span)[3]")
    # 来源渠道-列表返回的第四个
    source_channel_4 = (By.XPATH, "((//body/div)[last()]//li/span)[4]")
    # 来源渠道-列表返回的第五个
    source_channel_5 = (By.XPATH, "((//body/div)[last()]//li/span)[5]")
    # 来源渠道-列表返回的第六个
    source_channel_6 = (By.XPATH, "((//body/div)[last()]//li/span)[6]")
    # 来源渠道-列表返回的第七个
    source_channel_7 = (By.XPATH, "((//body/div)[last()]//li/span)[7]")
    # 来源渠道-列表返回的第八个
    source_channel_8 = (By.XPATH, "((//body/div)[last()]//li/span)[8]")
    # 来源渠道-列表返回的第九个
    source_channel_9 = (By.XPATH, "((//body/div)[last()]//li/span)[9]")
    # 来源渠道-列表返回的第十个
    source_channel_10 = (By.XPATH, "((//body/div)[last()]//li/span)[10]")
    # 来源渠道-列表返回的第十一个
    source_channel_11 = (By.XPATH, "((//body/div)[last()]//li/span)[11]")
    # 来源渠道-列表返回的第十二个 可能没有
    source_channel_12 = (By.XPATH, "((//body/div)[last()]//li/span)[12]")

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

    # 资源进展-待回电
    resource_progress_pre_phone = (By.XPATH, "//span[text()='待回电']")

    # 资源进展-已回电
    resource_progress_phoned = (By.XPATH, "//span[text()='已回电']")

    # 资源进展-已上门
    resource_progress_visit = (By.XPATH, "//span[text()='已上门']")

    # 资源进展-无法联系上
    resource_progress_uncall = (By.XPATH, "//span[text()='无法联系上']")

    # 资源进展-不再跟进/死单
    resource_progress_never = (By.XPATH, "//span[text()='不再跟进/死单']")

    # 首次上门日期
    first_visit_date = (By.XPATH, "(//input[@placeholder='选择日期'])[1]")

    # 首次上门日期-今天
    first_visit_date_today = (By.XPATH, "(//button[text()='今天'])[1]")

    # 首次上门日期-昨天
    first_visit_date_yesterday = (By.XPATH, "(//button[text()='昨天'])[2]")

    # 首次上门日期-一周前
    first_visit_date_last_week = (By.XPATH, "//button[text()='一周前']")

    # 最迟回访日期
    late_visit_date = (By.XPATH, "(//input[@placeholder='选择日期'])[2]")

    # 最迟回访日期-今天
    late_visit_date_today = (By.XPATH, "(//td[@class='available today'])[1]")

    # 年级
    collect_grade = (By.XPATH, "//input[@placeholder='请选择年级']")

    # 年级-小小班
    collect_grade_xxb = (By.XPATH, "//span[text()='小小班']")

    # 年级-高一
    collect_grade_senior = (By.XPATH, "(//body/div)[last()]//li[15]/span")

    # 班级
    resource_class = (By.XPATH, "//input[@placeholder='请填写班级,如五班']")

    # 就读学校
    school = (By.XPATH, "//input[@placeholder='请输入学校名称搜索']")

    # 就读学校 列表返回第一个
    school_name = (By.XPATH, "//body/div[last()]//ul/li/span")

    # 资源描述
    resource_desc = (By.XPATH, "//textarea[@placeholder='请填写资源描述,8~800中文字']")

    # 联系人关系文本
    contact_relationship_text = (By.XPATH, "//div[text()='联系人关系']")

    # 联系人关系
    contact_relationship = (By.XPATH, "(//input[@placeholder='请选择'])[1]")

    # 联系人关系-父亲
    contact_relationship_father = (By.XPATH, "//span[text()='父亲']")

    # 联系人关系-母亲
    contact_relationship_mother = (By.XPATH, "//span[text()='母亲']")

    # 联系人关系-亲戚
    contact_relationship_relation = (By.XPATH, "//span[text()='亲戚']")

    # 联系人关系-学员
    contact_relationship_self = (By.XPATH, "//span[text()='学员']")

    # 联系人关系-其他
    contact_relationship_other = (By.XPATH, "//span[text()='其他']")

    # 联系人姓名
    contact_name = (By.XPATH, "//input[@placeholder='请输入联系人姓名']")

    # 联系人手机/固话
    contact_phone = (By.XPATH, "//input[@placeholder='请输入联系手机/固话']")

    # 备注
    contact_remark = (By.XPATH, "//input[@placeholder='请输入备注']")

    # 性别-男
    resource_sex_male = (By.XPATH, "(//span[@class='el-radio__label'])[1]")

    # 性别-女
    resource_sex_female = (By.XPATH, "(//span[@class='el-radio__label'])[2]")

    # 生日
    resource_birthday = (By.XPATH, "(//input[@placeholder='选择日期'])[3]")

    # 推荐老师
    recommend_teacher = (By.XPATH, "//input[@placeholder='请输入老师姓名搜索']")

    # 推荐老师简称
    recommend_teacher_short = (By.XPATH, "//span[@class='small-font']")

    # 科目
    intention_subject = (By.XPATH, "//input[@placeholder='请选择科目']")

    # 科目-数学
    intention_subject_math = (By.XPATH, "//span[text()='数学']")

    # 地址/校区
    resource_address = (By.XPATH, "//input[@placeholder='请填写地址/小区']")

    # 确认添加
    confirm_add = (By.XPATH, "//button/span[text()='确认添加']")
