from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

#this script uses selenium to go through the snapchat.com UI and get the delivered/received status of a certin person. 
#Google Chrome must be installed on the host computer to run.
#replace the variables below with the correct values for your use-case

TargetSnapName=""
Username=""
Password=""

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://accounts.snapchat.com/accounts/v2/login?continue=%2Faccounts%2Fsso%3Freferrer%3Dhttps%253A%252F%252Fweb.snapchat.com%252F%253Fref%253Dsnapchat_dot_com_login_cta%26tiv_request_info%3DCmsKaQpnCkEE%252BZrN%252BpW%252BOmtFD0Lyd4ZxuNhoh17TcMSrD1SEsnc9fvRoIJvCJLXRgCUn6R9PA1WCaPtSFnbmu6Td11IiwevdJRIg7JMScchtn8n1ygLEMx61D%252BJfcvQ7L%252BESGE8M29IC2XcYCQ%253D%253D%26client_id%3Dweb-calling-corp--prod&tiv_request_info=CmsKaQpnCkEE%2BZrN%2BpW%2BOmtFD0Lyd4ZxuNhoh17TcMSrD1SEsnc9fvRoIJvCJLXRgCUn6R9PA1WCaPtSFnbmu6Td11IiwevdJRIg7JMScchtn8n1ygLEMx61D%2BJfcvQ7L%2BESGE8M29IC2XcYCQ%3D%3D")
driver.set_window_size(1000,1000)
WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.ID, 'accountIdentifier')))
elem = driver.switch_to.active_element
elem.send_keys(Username)
time.sleep(0.5)
elem.send_keys(Keys.ENTER)
WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.ID, 'password')))
elem = driver.switch_to.active_element
elem.send_keys(Password)
time.sleep(0.5)
elem.send_keys(Keys.ENTER)
WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CLASS_NAME, 'nonIntl')))
try:
    X=driver.find_element(By.CLASS_NAME, "cV8g1")
    X.click()
except:
    nothing=True
time.sleep(0.5)
elements = driver.find_elements(By.CLASS_NAME, 'nonIntl')
clairecount=0
correct=False
status=""
for element in elements:
    if TargetSnapName in element.text:
        clairecount+=1
        if clairecount==2:
            clairecount=0
            correct=True
    elif correct:
        status=element.text
        break
if status=="":
    print("target user not found")
else:
    print("Status: "+status)
