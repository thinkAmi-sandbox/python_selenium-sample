import traceback

import pytest
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

from index_page_object import IndexPageObject


class TestFindElement:
    def setup_method(self):
        self.chrome = Chrome()
        self.chrome.get('http://localhost:8000')

    def teardown_method(self):
        self.chrome.quit()

    def test_find_element_by_xxx(self):
        id1 = self.chrome.find_element_by_id('id1')
        assert id1.text == 'Text1'

        post1_1 = self.chrome.find_element_by_class_name('post1')
        assert post1_1.text == 'Post1-1'

        post1_2 = self.chrome.find_element_by_css_selector('.post1')
        assert post1_2.text == 'Post1-1'

        post1_3 = self.chrome.find_element_by_xpath('//li[@class="post1"]')
        assert post1_3.text == 'Post1-1'

    def test_find_elemnt_by_xxx_without_element(self):
        try:
            self.chrome.find_element_by_id('id2')
        except NoSuchElementException:
            print(f'\n{traceback.format_exc()}')

    def test_find_elements_by_xxx(self):
        id1 = self.chrome.find_elements_by_id('id1')
        assert len(id1) == 3
        assert id1[0].text == 'Text1'

        post1_1 = self.chrome.find_elements_by_class_name('post1')
        assert len(post1_1) == 2
        assert post1_1[0].text == 'Post1-1'

        post1_2 = self.chrome.find_elements_by_css_selector('.post1')
        assert len(post1_2) == 2
        assert post1_2[0].text == 'Post1-1'

        post1_3 = self.chrome.find_elements_by_xpath('//li[@class="post1"]')
        assert len(post1_3) == 2
        assert post1_3[0].text == 'Post1-1'

    def test_find_elements_by_xxx_without_element(self):
        post3 = self.chrome.find_elements_by_class_name('post3')
        assert len(post3) == 0

    def test_find_element(self):
        index_page = IndexPageObject(self.chrome)
        post = index_page.get_post_using_find_element()
        assert post == 'Post1-1'

    def test_find_element_without_element(self):
        with pytest.raises(NoSuchElementException):
            index_page = IndexPageObject(self.chrome)
            index_page.get_post_using_find_element_without_element()

    def test_find_elements(self):
        index_page = IndexPageObject(self.chrome)
        count = index_page.get_post_count_using_find_elements()
        assert count == 2

    def test_find_elements_without_element(self):
        index_page = IndexPageObject(self.chrome)
        count = index_page.get_post_count_using_find_elements_without_element()
        assert count == 0
