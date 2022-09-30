=== Description ===

Current version: 1.2.1

This program takes in a csv file and returns the LinkedIn links of the required people within that file.

This file contains 2 different functions for scraping, please avoid using OPTION 2 unless OPTION 1 breaks/does not work. 

=== Pre-Requisites ===

All files should be in the same directory (Including the .py file).

**Download and install Python(https://www.python.org/downloads/). This does not have to be in the same directory as the other files.

Download and install ChromeDriver(https://chromedriver.chromium.org/downloads). You will need to check your version of Chrome beforehand to download the respective version. To do so, go to Chrome and click on the 3 dots in the top-right of the screen. Select 'Settings', then 'About Chrome'. Put the executable into the same file/directory as everything else. If not, you will get the error message: selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home

Have a csv file named 'people.csv' with the fields 'first_name', 'last_name', 'company'.
(Names can be changed, see below)

Have the libraries selenium, pyautogui, pyperclip and pandas (See 'To Run' below)

=== To Run ===

First time:

Open command prompt and type cd filepath, with filepath being the path to where all the necessary files are located (including the csv file). Eg. cd Desktop/linkedin_scraper

Type pip install -r requirements.txt. This installs the required python libraries to run the code.

Every time:

Open command prompt and type cd filepath, with filepath being the path to where all the necessary files are located (including the csv file). Eg. cd Desktop/linkedin_scraper

Type python linkedin_scrape.py

=== Changes ===

If you have a different csv file name and headers, they may be changed on lines 147 (function call of scrape_from_csv() in main()) and 120 (try and except block, function call of scrape_function()) respectively.
The return file name may also be changed in the same place as the ingested csv file name. If you want to override the ingested file, then input the same file name. Filepath can also be changed here.

Un-comment line 135 if you don't want the pop-up (chrome_options.add_argument("--headless")). 

Change LinkedIn account details used for scraping on lines 144 and 145. LinkedIn may eventually detect that you are using a bot, so new accounts may have to be created. 

If for whatever reason you would like to use OPTION 2, then you may change the screen resolutions accordingly on lines 86 and 87, as it is not completely optimised yet. 
