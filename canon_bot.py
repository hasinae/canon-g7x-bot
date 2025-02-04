from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


# Configuration
TARGET_URL = "https://www.usa.canon.com/shop/p/powershot-g7-x-mark-ii?color=Black&type=New"
CHECK_INTERVAL = 60  # Check every 60 seconds
# CHANGE BELOW !!! CENSORED FOR PRIVACY!!!!!!
EMAIL = "example@gmail.com"
PASSWORD = "example"

# Function to check stock availability
def check_stock():
    response = requests.get(TARGET_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    stock_status = soup.find("div", {"class": "stock-status"})

    if stock_status and "in stock" in stock_status.text.lower():
        return True
    return False


# Function to automate purchase
# # def purchase_item():
#     # Set up Selenium WebDriver (make sure ChromeDriver is installed)
#     driver = webdriver.Chrome() 
#     driver.get(TARGET_URL)
    
#     try:
#         # Select color "Black"
#         color_dropdown = driver.find_element(By.ID, "color-select") 
#         color_dropdown.click()
#         black_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Black')]")
#         black_option.click()

#         # Add to cart
#         add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
#         add_to_cart_button.click()
        
#         # Proceed to checkout
#         checkout_button = driver.find_element(By.ID, "checkout-button")
#         checkout_button.click()
        
#         # Decline CarePAK coverage (assuming it's a checkbox or a button to decline)
#         carepak_decline_button = driver.find_element(By.XPATH, "//input[@name='carepak_decline']") 
#         if carepak_decline_button:
#             carepak_decline_button.click()

#         # Fill in checkout details (simplified)
#         email_field = driver.find_element(By.ID, "email")
#         email_field.send_keys(EMAIL)
        
#         password_field = driver.find_element(By.ID, "password")
#         password_field.send_keys(PASSWORD)
        
#         # Submit the form
#         submit_button = driver.find_element(By.ID, "submit-order-button")
#         submit_button.click()
        
#         # Check for confirmation page or success message
#         success_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Thank you for your order')]") 
#         if success_message:
#             print("Purchase completed successfully.")
#             return True
#         else:
#             print("Purchase attempt failed or did not complete as expected.")
#             return False
#     except Exception as e:
#         print(f"Error during purchase: {e}")
#         return False
#     finally:
#         # Close the browser
#         driver.quit()

def purchase_item(driver):
    driver.get(TARGET_URL)
    try:
        color_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "color-select"))
        )
        color_dropdown.click()
        black_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Black')]")
        black_option.click()
        
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )
        add_to_cart_button.click()
        
        checkout_button = driver.find_element(By.ID, "checkout-button")
        checkout_button.click()
        
        carepak_decline_button = driver.find_element(By.XPATH, "//input[@name='carepak_decline']")
        if carepak_decline_button:
            carepak_decline_button.click()

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(EMAIL)
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)
        
        submit_button = driver.find_element(By.ID, "submit-order-button")
        submit_button.click()
        
        success_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Thank you for your order')]")
        if success_message:
            print("Purchase completed successfully.")
            return True
        else:
            print("Purchase attempt failed or did not complete as expected.")
            return False
    except Exception as e:
        print(f"Error during purchase: {e}")
        return False


# Main loop
# def main():
#      # counter for stock checks
#     check_count = 0 
    
#     while True:
#         # Increment the counter for each stock check
#         check_count += 1 
        
#         if check_stock():
#             print(f"Checked {check_count} times now: Item is in stock! Attempting to purchase...")
#             success = purchase_item()
#             if success:
#                 break  # Stop after a successful purchase
#         else:
#             print(f"Checked {check_count} times now: Item is out of stock. Checking again in {CHECK_INTERVAL} seconds...")
#             time.sleep(CHECK_INTERVAL)

def main():
    check_count = 0 
    try:
        while True:
            check_count += 1 
            if check_stock():
                print(f"Checked {check_count} times now: Item is in stock! Attempting to purchase...")
                success = purchase_item(driver)
                if success:
                    break
            else:
                print(f"Checked {check_count} times now: Item is out of stock. Checking again in {CHECK_INTERVAL} seconds...")
                time.sleep(CHECK_INTERVAL)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
