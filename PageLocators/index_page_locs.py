#coding=gbk
from selenium.webdriver.common.by import By


class IndexPageLocs:

    # �������Ԫ��
    entrance = (By.XPATH, "//span[text()='�������']")

    # �ҵ���ԴԪ��
    my_resource = (By.XPATH, "//span[text()='�ҵ���Դ']")

    # �ҵ���Դ-��Ӫ��
    operation_depart = (By.XPATH, "//li/span[text()='��Ӫ��']")

    # �ҵ���Դ-ѧ�Ʋ�
    my_subject_depart = (By.XPATH, "//a[@href='/crm/my-resource/dis-dep']//span[text()='ѧ�Ʋ�']")

    # �ҵ���Դ-�г���
    my_market_depart = (By.XPATH, "//a[@href='/crm/my-resource/marketdep']//span[text()='�г���']")

    # ������Դ
    depart_resource = (By.XPATH, "//span[text()='������Դ']")

    # ������Դ-ѧ�Ʋ�
    depart_subject = (By.XPATH, "//a[@href='/crm/dept-resource/dis-dep']//span[text()='ѧ�Ʋ�']")
    # ������Դ-�г���
    depart_market = (By.XPATH, "//a[@href='/crm/dept-resource/marketdep']//span[text()='�г���']")

    # У����Դ
    branch_resource = (By.XPATH, "//a[@href='/crm/schoolresource']/li")

    # ��Դת��
    resource_transfer = (By.XPATH, "//span[text()='��Դת��']")

    # ��Դ���
    resource_unbind = (By.XPATH, "//span[text()='��Դ���']")

    # Լ�ù���
    appointment_manage = (By.XPATH, "//span[text()='Լ�ù���']")

    # У��
    branch = (By.XPATH, "//span[@class='title']/following-sibling::span")














