from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import schedule
import subprocess
import platform

# The list of dates and times you want to run this job
job_schedule = ['16/6/2023 18:55', '21/6/2023 18:55', '23/6/2023 18:55', '30/6/2023 18:55', 
                '03/7/2023 18:55', '05/7/2023 18:55', '07/7/2023 18:55', '08/7/2023 18:55',
                '10/7/2023 18:55', '11/7/2023 18:55', '12/7/2023 18:55', '13/7/2023 18:55',
                '14/7/2023 18:55']  

# Path to the chromedriver executable
chromedriver_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'  

username = 'username'
password = 'password'

def job():
    # Create a new instance of the Google Chrome driver
    driver = webdriver.Chrome(executable_path=chromedriver_path)

    # Go to the login page
    driver.get('https://login/page')

    # Find the login form and submit it
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('loginbtn').click()

    time.sleep(3)  # Wait for the page to load

    # Go to the specified course page
    driver.get('https://page/with/all/lectures')

    time.sleep(3)  # Wait for the page to load

    # Find the relevant date/time span
    section_modules = driver.find_element_by_class_name('section-modules')
    spans = section_modules.find_elements_by_tag_name('span')

    # Get the current date and time
    now = datetime.datetime.now()

    # Convert the current date/time to a string in the format used by the spans
    now_str = now.strftime('%d/%m/%Y, %H:%M')

    for span in spans:
        # If the span's text matches the current date/time, click its parent link
        if span.text == now_str:
            parent_link = span.find_element_by_xpath('..')
            if 'aalink' in parent_link.get_attribute('class'):
                parent_link.click()

                time.sleep(3)  # Wait for the page to load

                # Click the 'Join Meeting' button
                table = driver.find_element_by_class_name('generaltable')
                button = table.find_element_by_tag_name('button')
                if 'btn-primary' in button.get_attribute('class'):
                    button.click()

                break  # Exit the loop as we have found and clicked the correct span

    # Quit the driver
    driver.quit()

    # Kill Zoom process after 3 hours or at 22:00
    end_time = datetime.datetime.now() + datetime.timedelta(hours=3)
    if end_time.hour > 22:
        end_time = end_time.replace(hour=22, minute=0, second=0, microsecond=0)

    while datetime.datetime.now() < end_time:
        time.sleep(1)  # Wait a second before checking the time again

    # Kill the Zoom process
    if platform.system() == "Windows":
        subprocess.run(['taskkill', '/IM', 'Zoom.exe', '/F'])
    else:
        subprocess.run(['pkill', 'Zoom'])

# Schedule the job at the specified times
for job_time in job_schedule:
    date_time_obj = datetime.datetime.strptime(job_time, '%d/%m/%Y %H:%M')
    schedule.every().day.at(date_time_obj.time().strftime("%H:%M")).do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
