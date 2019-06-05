from selenium import webdriver
import time

email = 'surfer.zoke@gmail.com' ##inputs for account
password = 'Burrito1'
browser = webdriver.Edge("MicrosoftWebDriver.exe") ##loads driver
browser.implicitly_wait(5)
count = 0

def login():
    browser.get('http://www.quora.com')

    fields = browser.find_elements_by_class_name("text header_login_text_box ignore_interaction")  # selects the login text fields
    fields[0].send_keys(email)
    fields[1].send_keys(password)

    login = browser.find_element_by_class_name('submit_button ignore_interaction')
    login.click()  # logs in

def setting():
    browser.get('https://www.quora.com/profile/Tom-Pierre-1/questions')  # heads to question page

    profile_counts = browser.find_elements_by_class_name('list_count')
    question_count = int(profile_counts[1].text)
    for i in range(1, 5):#normally question_count

        questions = browser.find_elements_by_class_name('ui_content_title ui_content_title--default ui_content_title--medium')
        while i >= len(questions):
            browser.execute_script('window.scrollBy(0, 110)')
            questions = browser.find_elements_by_class_name('ui_content_title ui_content_title--default ui_content_title--medium')
        print(questions[i].text, i)

        questions[(i)].click()
        questionPage = browser.window_handles[1] ##changes browser tab
        browser.switch_to.window(questionPage)
        requesting()
        browser.close()
        browser.switch_to.window(browser.window_handles[0]) # heads back to question page

def requesting():
    request = browser.find_elements_by_id('request') #Even though there is only one requets element will be present, array is returned so that it can be counted to determine whether request is present. Selenium does not allow to check for single element without returning error
    while (len(request)!=0): #runs loop as long as request is still visible
        request[0].click()
        request = browser.find_elements_by_id('request')
    time.sleep(.3)
    buttons = browser.find_elements_by_class_name('u-flex-none u-relative u-flex-align-self--center button_wrapper')
    users = browser.find_elements_by_class_name('user')  # to look cool shows names and stuff
    buttoncount = len(buttons)
    if buttoncount > 50:
        buttoncount = 50

    for x in range(0, buttoncount, 2):
        browser.execute_script("arguments[0].scrollIntoView(true);", buttons[(x)])
        buttons[x].click()  ##must be even for whatever reason
        global count
        count +=1
        print('Requested ' + users[x].text + ' ' + str(count))


def submit():
    submit = browser.find_elements_by_class_name('submit_button modal_action')
    submit[2].click()

login()
setting()





