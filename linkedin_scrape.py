import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui as pag
import pyperclip
import pandas as pd

""" Two implementations of searching LinkedIn for a person using their first name, last name and company, and returning
    their LinkedIn link.
    Only works for the first person found in the LinkedIn search results"""

""" Popup that prompts for the three fields - first name, last name and company """
def popup():
    print('Please enter First Name:')
    first_name = input()

    print('Please enter Last Name:')
    last_name = input()

    print('Please enter Company:')
    company = input()

    return (first_name, last_name, company)

""" Use selenium to login to LinkedIn
    Pre-requisites: username and password, driver
    May encounter additional popup when LinkedIn thinks you're a bot """
def linkedin_login(username, password, driver):

    driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')

    # find username/email field and send the username itself to the input field
    driver.find_element(By.ID, "username").send_keys(username) 
    # find password input field and insert password as well
    driver.find_element(By.ID, "password").send_keys(password)
    # click login button
    sleep(1)
    driver.find_element(By.CLASS_NAME, "login__form_action_container").click()

""" OPTION 1

    Using selenium to get the required data from LinkedIn 

    Pre-requisites: specified driver, first name, last name and company

    Returns LinkedIn link """
def single_scrape_selenium(driver, first_name, last_name, company):

    # Search for the desired person
    url = 'https://www.linkedin.com/search/results/people/?keywords='+first_name+'%20'+last_name+'%20'+company+'&origin=GLOBAL_SEARCH_HEADER'
    driver.get(url)

    # Click on the first result
    element = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.linkedin.com/in/')]")
    #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'linkedin')]")))
    driver.execute_script("arguments[0].click();", element)

    sleep(1)

    # Get the current URL and return it
    val = driver.current_url
    return val

""" OPTION 2 (Try not to use)

    Using pyautogui to click on the first result, and get the link for that result

    Pre-requisite: Specified driver, need to have logged in to LinkedIn, and Chrome must open on the 
    same screen as code, due to pyautogui constraints for multiple displays

    Returns LinkedIn link """
def single_scrape_pag(driver, first_name, last_name, company):

    url = 'https://www.linkedin.com/search/results/people/?keywords='+first_name+'%20'+last_name+'%20'+company+'&origin=GLOBAL_SEARCH_HEADER'

    webbrowser.open(url)

    # Can change sleep values if necessary

    # Get size of screen
    size_x, size_y = pag.size()

    goto_x = 420/1920 * size_x
    goto_y = 300/1100 * size_y

    # Click on first result
    sleep(2.5)
    pag.click(goto_x,goto_y) 
    
    # Click on URL
    sleep(1)
    pag.click(200/1920 * size_x, 50/1100 * size_y)

    # Copy URL
    pag.hotkey('ctrl', 'c')

    # Close the tab
    #sleep(0.1)
    pag.hotkey('ctrl', 'w')

    # Get copied value from clipboard
    val = pyperclip.paste()
    return val

""" Pre-requisites: Takes in the username and password for login to LinkedIn, the scrape function (either of the two defined above), 
    the file which contains the data, and the specified driver 
    
    Returns a new file in code's directory with a new column, 'LinkedIn', populated with the LinkedIn links accordingly"""
def scrape_from_csv(username, password, scrape_function, csv_file_handle, return_file, driver):
    df = pd.read_csv(csv_file_handle)
    linkedin_list = []
    linkedin_login(username, password, driver)
    
    # Deals with what happens when there are no results for the person you are looking for
    for index, row in df.iterrows():
        try:
            val = scrape_function(driver, row['first_name'], row['last_name'], row['company'])
        except:
            linkedin_list.append('Person Not Found')
            continue
        linkedin_list.append(val)
    df['linkedin'] = linkedin_list
  
    df.to_csv(return_file, index = False)    

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    #This line prevents the pop-up
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    # Account Details
    username = # Input LinkedIn username
    password = # Input LinkedIn password

    scrape_from_csv(username, password, single_scrape_selenium, 'people.csv', 'new_people.csv', driver)

if __name__ == "__main__":
    main()


""" Further improvements to be made in the future:
    - Deal with what happens when LinkedIn thinks you're a bot (which you are) """

""" Code written by Chong Ke-Ming """
