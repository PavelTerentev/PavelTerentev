def test_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element_by_xpath('//article//form/button')



# pytest --language=es test_items.py


