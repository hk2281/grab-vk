from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import json 
import sys


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


driver.get("https://vk.com/feed")
log = driver.find_element_by_id("email")
log.send_keys("")
pas = driver.find_element_by_id("pass")
pas.send_keys("")
pas.send_keys(Keys.RETURN)

try:
  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.title_is("Новости"))
  print("hi")
  driver.get("https://vk.com/audios")
  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.title_is("Моя музыка"))
  arr = driver.execute_script('let tracks = new Set();let nodes = [...document.querySelectorAll(".audio_row")];nodes.forEach((nodeCur) => {const trackName = nodeCur.querySelector(".audio_row__title_inner").firstChild.textContent;const bandName = nodeCur.querySelector(".audio_row__performers > a").firstChild.textContent;const name = {aname: trackName, bName: bandName};tracks.add(name);});let arr = JSON.stringify(Array.from(tracks));return arr')
  lis = json.loads(arr)

  for i in range(int(sys.argv[1])):
    print(lis[i])

  
    

finally:
  print('f')

# driver.execute_script("alert('hi')");

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
