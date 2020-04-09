import selenium
from Python_Selenium import fileutil
from selenium import webdriver
from Python_Selenium import config

driver=webdriver.Chrome(executable_path="D:/Drivers/chromedriver_win32/chromedriver.exe")
driver.get(config.url)
excel_path="D://InterviewPrep//testdata.xlsx"

total_rows=fileutil.total_rows(excel_path,'Sheet1')
#total_cols=fileutil.total_cols(excel_path,'Sheet1')
res_col=3
for r in range(2,total_rows+1):
    username = fileutil.read_data_from_excel(excel_path, 'Sheet1', r, 1)
    password = fileutil.read_data_from_excel(excel_path, 'Sheet1', r, 2)
    wb1=driver.find_element_by_id('email')
    wb1.clear()
    wb1.send_keys(username)
    wb2=driver.find_element_by_id('pass')
    wb2.clear()
    wb2.send_keys(password)
    fileutil.write_data_into_excel(excel_path,'Sheet1',r,res_col,'Pass')






