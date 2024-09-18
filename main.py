from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless") 

chrome_driver_path = "/path/to/chromedriver"  

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


url = "https://www.dexscreener.com/new-tokens"
driver.get(url)


driver.implicitly_wait(10)  


tokens = driver.find_elements(By.CLASS_NAME, 'token-info')  

new_tokens = []
for token in tokens:
    token_name = token.find_element(By.TAG_NAME, 'h2').text 
    token_address = token.find_element(By.CLASS_NAME, 'contract-link').text  
    new_tokens.append({
        'name': token_name,
        'contract_address': token_address
    })

driver.quit()

for token in new_tokens:
    print(f"Token: {token['name']}, Contract Address: {token['contract_address']}")
