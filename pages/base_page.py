from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        return self.driver.current_url

"""
Common WebDriver calls:

For WebDriver:

    driver.get("https://www.google.com")
    driver.find_element_by_id("lst-ib").send_keys("Hello World")
    driver.find_element_by_name("btnK").click()
    driver.find_element_by_link_text("Hello World - Wikipedia").click()
    driver.find_element_by_partial_link_text("Hello World").click()
    driver.find_element_by_xpath("//a[contains(text(),'Hello World')]").click()
    driver.find_element_by_css_selector("a[href='https://en.wikipedia.org/wiki/%22Hello,_World!%22_program']").click()
    driver.find_element_by_class_name("mw-redirect").click()
    driver.find_element_by_tag_name("a").click()

    driver.current_url
    driver.title
    driver.page_source
    driver.close()
    driver.quit()

    driver.maximize_window()

For Elements:

    clear()
    click()
    get_attribute('attribute_name')
    is_displayed()
    is_enabled()
    is_selected()
    send_keys('Hello World')
    submit()
    location
    size
    text
    get_property('property_name')

For WebDriverWait:

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
    element.click()

For Select:

    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_id('someid'))
    select.select_by_visible_text('Banana')
    select.select_by_index(1)
    select.select_by_value('1')

For ActionChains:

    from selenium.webdriver.common.action_chains import ActionChains
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    action.click(element).perform()
    action.click_and_hold(element).perform()
    action.context_click(element).perform()
    action.double_click(element).perform()
    action.drag_and_drop(element, target).perform()
    action.move_by_offset(10, 20).perform()
    action.move_to_element(element).perform()
    action.release(element).perform()
    action.send_keys('Hello World').perform()
    action.send_keys(Keys.ENTER).perform()
    action.send_keys_to_element(element, 'Hello World').perform()
    action.send_keys_to_element(element, Keys.ENTER).perform()
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

For JavaScriptExecutor:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
    driver.execute_script("window.open('https://www.google.com');")

For Cookies:

    driver.get_cookies()
    driver.get_cookie('cookie_name')
    driver.delete_cookie('cookie_name')
    driver.delete_all_cookies()
    driver.add_cookie({'name': 'foo', 'value': 'bar'})

For Alerts:

    alert = driver.switch_to.alert
    alert.accept()
    alert.dismiss()
    alert.send_keys('Hello World')
    alert.text

For Frames:

    driver.switch_to.frame('frame_name')
    driver.switch_to.frame(1)
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    driver.switch_to.default_content()

For Windows:

    driver.switch_to.window('window_name')
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.window(driver.window_handles[1])

For Navigation:

    driver.back()
    driver.forward()
    driver.refresh()

For Options:

    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

For DesiredCapabilities:

    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "normal"
    driver = webdriver.Firefox(desired_capabilities=caps)

For Proxy:

    from selenium.webdriver.common.proxy import Proxy, ProxyType
    proxy = Proxy()

"""