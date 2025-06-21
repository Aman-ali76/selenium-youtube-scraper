import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://youtube.com")
    time.sleep(3)

    box = driver.find_element(By.NAME, "search_query")
    box.send_keys("Selenium Python Tutorial")
    box.send_keys(Keys.RETURN)
    time.sleep(2)

    def scroller(min_videos=50):
        last_height = driver.execute_script("return document.documentElement.scrollHeight")

        while True:
            try:
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
                time.sleep(2)

                video_containers = driver.find_elements(By.CLASS_NAME, "style-scope ytd-item-section-renderer")
                print(f"Video : {len(video_containers)} Scraped")

                if len(video_containers) >= min_videos:
                    break

                new_height = driver.execute_script("return document.documentElement.scrollHeight")
                last_height = new_height

            except Exception as e:
                print(f"Error while scrolling: {e}")

    scroller()

    video_html = [container.get_attribute('outerHTML') for container in driver.find_elements(By.CLASS_NAME, "style-scope ytd-item-section-renderer")]

    for num,item in enumerate(video_html):
        with open(f"videos-{num}.html", "a") as file:
            file.write(f"{item} \n")


except KeyboardInterrupt:
    print("\nTerminated by user.")

finally:

    driver.quit()
    print("Browser Closed.")