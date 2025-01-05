import random
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

# Specify the path to your ChromeDriver executable
chromedriver_path = 'D:\\chrome\\chromedriver-win32\\chromedriver.exe'
service = Service(chromedriver_path)

# Pass the service object to the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open the website and maximize the window
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

# Select phone button
phone = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[text()="Phones & PDAs"]'))
)
phone.click()

# Select iPhone
iphone = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[text()="iPhone"]'))
)
iphone.click()
time.sleep(1)

# First picture
first_pic = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//ul[@class="thumbnails"]/li[1]'))
)
first_pic.click()
time.sleep(2)

# Click next button 5 times
next_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@title="Next (Right arrow key)"]'))
)

for _ in range(5):
    next_click.click()
    time.sleep(2)

# Save screenshot and close image view
driver.save_screenshot('screenshot' + str(random.randint(0, 101)) + '.png')
x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(2)

# Phone quantity
quantity = driver.find_element(By.ID, 'input-quantity')
quantity.clear()
quantity.send_keys('2')
time.sleep(1)

# Add to cart button
add_to_button = driver.find_element(By.ID, 'button-cart')
add_to_button.click()
time.sleep(2)

# Navigate to laptops
action = ActionChains(driver)
laptops = driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
action.move_to_element(laptops).perform()
time.sleep(2)

laptops_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]'))
)
laptops_2.click()

# Select HP LP3065
hp = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[text()="HP LP3065"]'))
)
hp.click()

#click button
add_to_button_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'button-cart'))
)
add_to_button_2.location_once_scrolled_into_view
time.sleep(1)

# Calendar
calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar = driver.find_element(By.XPATH, '//th[@class="next"]')
month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')

# Year 2025 month : January
while month_year.text != 'January 2025':
    next_click_calendar.click()

# Select day 3
calendar_date = driver.find_element(By.XPATH, '//td[text()="3"]')
calendar_date.click()
time.sleep(1)

# Click add to cart button
add_to_button_2.click()
time.sleep(1)

# Checkout
go_to_cart = driver.find_element(By.ID, 'cart-total')
go_to_cart.click()
time.sleep(3)

checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//p[@class="text-right"]/a[2]'))
)
checkout.click()
time.sleep(1)

# Remove product
remove = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-times-circle"]'))
)
remove.click()
time.sleep(1)

# Checkout again
checkout_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Checkout")]'))
)
checkout_2.click()
time.sleep(1)

# Guest checkout
driver.find_element(By.XPATH, '//input[@value="guest"]').click()
driver.find_element(By.ID, 'button-account').click()
time.sleep(1)

# Billing details
driver.find_element(By.ID, 'input-payment-firstname').send_keys('sachini')
driver.find_element(By.ID, 'input-payment-lastname').send_keys('tharindi')
driver.find_element(By.ID, 'input-payment-email').send_keys('sachini@gmail.com')
driver.find_element(By.ID, 'input-payment-telephone').send_keys('0712347789')
driver.find_element(By.ID, 'input-payment-address-1').send_keys('malabe, srilanka')
driver.find_element(By.ID, 'input-payment-city').send_keys('Frankfurt')
driver.find_element(By.ID, 'input-payment-postcode').send_keys('10115')

# Country and region
# Select "Sri Lanka" by visible text
country = Select(driver.find_element(By.ID, 'input-payment-country'))
country.select_by_visible_text('Sri Lanka')
time.sleep(1)


# Select "Western" as the region
region = Select(driver.find_element(By.ID, 'input-payment-zone'))
region.select_by_visible_text('Western')  # Select Western from the region list
time.sleep(1)

# Click continue 2
continue_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'button-guest'))
)
continue_2.click()
time.sleep(1)

# Click continue 3
continue_3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'button-shipping-method'))
)
continue_3.click()
time.sleep(1)

# Accept terms & conditions
terms = driver.find_element(By.XPATH, '//input[@name="agree"]')
terms.click()
time.sleep(1)

# Click continue 4
continue_4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'button-payment-method'))
)
continue_4.click()
time.sleep(3)

# Final price
final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
print("The final price is " + final_price.text)
time.sleep(2)

# Confirm order
confirmation_button = driver.find_element(By.ID, 'button-confirm')
confirmation_button.click()
time.sleep(2)

# Success text
success_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="col-sm-12"]/h1'))
)
print(success_text.text)
time.sleep(1)

# Add a delay to observe the result
time.sleep(10)

# Close the browser
driver.close()
