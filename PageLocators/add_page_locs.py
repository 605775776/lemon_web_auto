#coding=gbk
# �����Դҳ��Ԫ�ض�λ



from selenium.webdriver.common.by import By


class AddPageLocs:

    # ѧ������
    student_name = (By.XPATH, "//input[@placeholder='����дѧ������']")
    # ��Դ����
    resource_type = (By.XPATH, "//input[@placeholder='��ѡ����Դ����']")

    # ��Դ����-У��ǰ̨�绰
    resource_type_1 = (By.XPATH, "//li/span[text()='У��ǰ̨�绰']")
    # ��Դ����-�ٷ�
    resource_type_2 = (By.XPATH, "//li/span[text()='�ٷ�']")
    # ��Դ����-�ܲ�����
    resource_type_3 = (By.XPATH, "//li/span[text()='�ܲ�����']")
    # ��Դ����-�ܲ�������Դ
    resource_type_4 = (By.XPATH, "//li/span[text()='�ܲ�������Դ']")
    # ��Դ����-ѧ��ʦ�ھ�/ת����
    resource_type_5 = (By.XPATH, "//li/span[text()='ѧ��ʦ�ھ�/ת����']")
    # ��Դ����-�γ̹���/��ѯʦ�ھ���Դ
    resource_type_6 = (By.XPATH, "//li/span[text()='�γ̹���/��ѯʦ�ھ���Դ']")

    # ��Դ����
    source_channel = (By.XPATH, "//input[@placeholder='��ѡ����Դ����']")

    # ��Դ���� �б��صĵ�һ�� [last()]
    source_channel_1 = (By.XPATH, "(//body/div)[last()]//li/span")
    # ��Դ����-�б��صĵڶ���
    source_channel_2 = (By.XPATH, "((//body/div)[last()]//li/span)[2]")
    # ��Դ����-�б��صĵ�����
    source_channel_3 = (By.XPATH, "((//body/div)[last()]//li/span)[3]")
    # ��Դ����-�б��صĵ��ĸ�
    source_channel_4 = (By.XPATH, "((//body/div)[last()]//li/span)[4]")
    # ��Դ����-�б��صĵ����
    source_channel_5 = (By.XPATH, "((//body/div)[last()]//li/span)[5]")
    # ��Դ����-�б��صĵ�����
    source_channel_6 = (By.XPATH, "((//body/div)[last()]//li/span)[6]")
    # ��Դ����-�б��صĵ��߸�
    source_channel_7 = (By.XPATH, "((//body/div)[last()]//li/span)[7]")
    # ��Դ����-�б��صĵڰ˸�
    source_channel_8 = (By.XPATH, "((//body/div)[last()]//li/span)[8]")
    # ��Դ����-�б��صĵھŸ�
    source_channel_9 = (By.XPATH, "((//body/div)[last()]//li/span)[9]")
    # ��Դ����-�б��صĵ�ʮ��
    source_channel_10 = (By.XPATH, "((//body/div)[last()]//li/span)[10]")
    # ��Դ����-�б��صĵ�ʮһ��
    source_channel_11 = (By.XPATH, "((//body/div)[last()]//li/span)[11]")
    # ��Դ����-�б��صĵ�ʮ���� ����û��
    source_channel_12 = (By.XPATH, "((//body/div)[last()]//li/span)[12]")

    # ��Դ����
    collect_date = (By.XPATH, "//input[@placeholder='ѡ������ʱ��']")

    # ��Դ����Ϊ����
    collect_date_today = (By.XPATH, "//button[text()='����']")

    # ��Դ����Ϊ����
    collect_date_yesterday = (By.XPATH, "//button[text()='����']")

    # ��Դ����Ϊһ��ǰ
    collect_date_last_week = (By.XPATH, "//button[text()='һ��ǰ']")

    # ��Դ����
    resource_stars = (By.XPATH, "//span[@class='el-rate__item'][5]")

    # ��Դ��չ
    resource_progress = (By.XPATH, "//input[@placeholder='��ѡ����Դ��չ']")

    # ��Դ��չ-���ص�
    resource_progress_pre_phone = (By.XPATH, "//span[text()='���ص�']")

    # ��Դ��չ-�ѻص�
    resource_progress_phoned = (By.XPATH, "//span[text()='�ѻص�']")

    # ��Դ��չ-������
    resource_progress_visit = (By.XPATH, "//span[text()='������']")

    # ��Դ��չ-�޷���ϵ��
    resource_progress_uncall = (By.XPATH, "//span[text()='�޷���ϵ��']")

    # ��Դ��չ-���ٸ���/����
    resource_progress_never = (By.XPATH, "//span[text()='���ٸ���/����']")

    # �״���������
    first_visit_date = (By.XPATH, "(//input[@placeholder='ѡ������'])[1]")

    # �״���������-����
    first_visit_date_today = (By.XPATH, "(//button[text()='����'])[1]")

    # �״���������-����
    first_visit_date_yesterday = (By.XPATH, "(//button[text()='����'])[2]")

    # �״���������-һ��ǰ
    first_visit_date_last_week = (By.XPATH, "//button[text()='һ��ǰ']")

    # ��ٻط�����
    late_visit_date = (By.XPATH, "(//input[@placeholder='ѡ������'])[2]")

    # ��ٻط�����-����
    late_visit_date_today = (By.XPATH, "(//td[@class='available today'])[1]")

    # �꼶
    collect_grade = (By.XPATH, "//input[@placeholder='��ѡ���꼶']")

    # �꼶-СС��
    collect_grade_xxb = (By.XPATH, "//span[text()='СС��']")

    # �꼶-��һ
    collect_grade_senior = (By.XPATH, "(//body/div)[last()]//li[15]/span")

    # �༶
    resource_class = (By.XPATH, "//input[@placeholder='����д�༶,�����']")

    # �Ͷ�ѧУ
    school = (By.XPATH, "//input[@placeholder='������ѧУ��������']")

    # �Ͷ�ѧУ �б��ص�һ��
    school_name = (By.XPATH, "//body/div[last()]//ul/li/span")

    # ��Դ����
    resource_desc = (By.XPATH, "//textarea[@placeholder='����д��Դ����,8~800������']")

    # ��ϵ�˹�ϵ�ı�
    contact_relationship_text = (By.XPATH, "//div[text()='��ϵ�˹�ϵ']")

    # ��ϵ�˹�ϵ
    contact_relationship = (By.XPATH, "(//input[@placeholder='��ѡ��'])[1]")

    # ��ϵ�˹�ϵ-����
    contact_relationship_father = (By.XPATH, "//span[text()='����']")

    # ��ϵ�˹�ϵ-ĸ��
    contact_relationship_mother = (By.XPATH, "//span[text()='ĸ��']")

    # ��ϵ�˹�ϵ-����
    contact_relationship_relation = (By.XPATH, "//span[text()='����']")

    # ��ϵ�˹�ϵ-ѧԱ
    contact_relationship_self = (By.XPATH, "//span[text()='ѧԱ']")

    # ��ϵ�˹�ϵ-����
    contact_relationship_other = (By.XPATH, "//span[text()='����']")

    # ��ϵ������
    contact_name = (By.XPATH, "//input[@placeholder='��������ϵ������']")

    # ��ϵ���ֻ�/�̻�
    contact_phone = (By.XPATH, "//input[@placeholder='��������ϵ�ֻ�/�̻�']")

    # ��ע
    contact_remark = (By.XPATH, "//input[@placeholder='�����뱸ע']")

    # �Ա�-��
    resource_sex_male = (By.XPATH, "(//span[@class='el-radio__label'])[1]")

    # �Ա�-Ů
    resource_sex_female = (By.XPATH, "(//span[@class='el-radio__label'])[2]")

    # ����
    resource_birthday = (By.XPATH, "(//input[@placeholder='ѡ������'])[3]")

    # �Ƽ���ʦ
    recommend_teacher = (By.XPATH, "//input[@placeholder='��������ʦ��������']")

    # �Ƽ���ʦ���
    recommend_teacher_short = (By.XPATH, "//span[@class='small-font']")

    # ��Ŀ
    intention_subject = (By.XPATH, "//input[@placeholder='��ѡ���Ŀ']")

    # ��Ŀ-��ѧ
    intention_subject_math = (By.XPATH, "//span[text()='��ѧ']")

    # ��ַ/У��
    resource_address = (By.XPATH, "//input[@placeholder='����д��ַ/С��']")

    # ȷ�����
    confirm_add = (By.XPATH, "//button/span[text()='ȷ�����']")
