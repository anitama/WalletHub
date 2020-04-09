from Python_Selenium import fileutil
from selenium import webdriver
from Python_Selenium import config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:/Drivers/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(config.wallethub_url)
action=ActionChains(driver)
web_ele=driver.find_element_by_xpath("//div[@class='review-action ng-enter-element']//div[@class='rating-box-wrapper']")
action.move_to_element(web_ele).perform()
web_ele.click()
driver.find_element_by_xpath("//div[@class='dropdown second']//span[@class='dropdown-placeholder']").click()
driver.find_element_by_xpath("//div[@class='wrev-user-input-box input-field progress-indicator-container']//ul[@class='dropdown-list ng-enter-element']/li[2]").click()
driver.find_element_by_xpath("//textarea[@placeholder='Write your review...']").send_keys("This is the review for Health Insurance. This is the review for Health Insurance. This is the review for Health Insurance. This is the review for Health Insurance. This is the review for Health Insurance")
driver.find_element_by_xpath("//div[@class='sbn-action semi-bold-font btn fixed-w-c tall']").click()


