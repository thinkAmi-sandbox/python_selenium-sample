from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import traceback


class IndexPageObject:
    # Seleniumで探す要素をクラス定数として定義する
    ID1 = (By.ID, 'id1')
    CLASS1 = (By.CLASS_NAME, 'post1')
    CLASS2 = (By.CLASS_NAME, 'post2')
    CLASS3 = (By.CLASS_NAME, 'post3')  # これは存在しない要素
    CSS = (By.CSS_SELECTOR, '.post1')
    XPATH = (By.XPATH, '//li[@class="post1"]')

    def __init__(self, driver: WebDriver):
        # WebDriverをインスタンスに渡す
        self.driver = driver

    def get_post_using_find_element(self):
        # IDで探す場合
        id1 = self.driver.find_element(*IndexPageObject.ID1)
        # クラス名で探す場合
        class1 = self.driver.find_element(*IndexPageObject.CLASS1)
        # CSSセレクタで探す場合
        css1 = self.driver.find_element(*IndexPageObject.CSS)
        # XPATHで探す場合
        xpath1 = self.driver.find_element(*IndexPageObject.XPATH)

        # 本来、PageObjectではassertは不要
        # 今回はサンプルということで、それぞれ正しいテキストが取れているかを確認する
        assert id1.text == 'Text1'
        assert class1.text == 'Post1-1'
        assert css1.text == 'Post1-1'
        assert xpath1.text == 'Post1-1'
        # どれでも同じなので、適当なのを返す
        return xpath1.text

    def get_post_using_find_element_without_element(self):
        try:
            # find_element()の場合、要素が存在しないと例外が送出される
            return self.driver.find_element(*IndexPageObject.CLASS3)
        except NoSuchElementException:
            print(f'\n{traceback.format_exc()}')
            raise

    def get_post_count_using_find_elements(self):
        # IDで探す場合
        id1 = self.driver.find_elements(*IndexPageObject.ID1)
        # クラス名で探す場合
        class1 = self.driver.find_elements(*IndexPageObject.CLASS1)
        # CSSセレクタで探す場合
        css1 = self.driver.find_elements(*IndexPageObject.CSS)
        # XPATHで探す場合
        xpath1 = self.driver.find_elements(*IndexPageObject.XPATH)

        # 本来、PageObjectではassertは不要
        # 今回はサンプルということで、それぞれ正しい件数が取れているかを確認する
        assert len(id1) == 3
        assert len(class1) == 2
        assert len(css1) == 2
        assert len(xpath1) == 2
        # どれでも同じなので、適当なのを返す
        return len(xpath1)

    def get_post_count_using_find_elements_without_element(self):
        # find_elements()の場合は、要素が存在しなくても例外とならず、長さ0のリストが返る
        elements = self.driver.find_elements(*IndexPageObject.CLASS3)
        assert len(elements) == 0
        return len(elements)
