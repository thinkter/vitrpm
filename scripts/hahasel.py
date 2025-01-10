import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)




driver.get("https:reddit.com/r/vit/new")

# Scroll function
def scroll_to_load_all_posts(driver, wait_time=5, max_scrolls=50):
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0
    
    while scrolls < max_scrolls:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new content to load
        time.sleep(wait_time)
        
        # Check the new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If the height hasn't changed, assume no new content is loading
            print("No more posts to load.")
            break
        
        last_height = new_height
        scrolls += 1
        print(f"Scrolled {scrolls} times.")

# Call the function to load all posts
'''
scroll_to_load_all_posts(driver)



elements = driver.find_elements(By.CSS_SELECTOR, 'a[slot="full-post-link"]')


print(f"Found {len(elements)} elements with slot attribute.")
for index, element in enumerate(elements):
    print(f"Element {index + 1}:")
    print(f"  Text: {element.text}")
    print(f"  URL: {element.get_attribute('href')}")

'''
for i in range(10):
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[slot="full-post-link"]')
    scroll_to_load_all_posts(driver,wait_time=5,max_scrolls=2)
    print(f"Found {len(elements)} elements with slot attribute.")
    for index, element in enumerate(elements):
        print(f"Element {index + 1}:")
        print(f"  Text: {element.text}")
        print(f"  URL: {element.get_attribute('href')}")
        with open('urls.txt',a) as f:
            f.write(element.get_attribute('href'))
driver.quit()
