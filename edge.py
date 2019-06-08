from selenium import webdriver
import time

email = 'surfer.zoke@gmail.com' ##inputs for account
password = 'Burrito1'
count = 0
browser = webdriver.Edge("MicrosoftWebDriver.exe")  ##intiates browser variable
browser.implicitly_wait(5)
'''''
Functions used for Testting
'''''

def question_page():##goes to question page
    browser.get('https://www.quora.com/profile/Tom-Pierre-1/questions')  # heads to question page

def question1():##test set up for unrequested function
    browser.get('https://www.quora.com/How-do-I-know-if-my-kid-drinks')

def question2(): ##test set up for already requested function
    browser.get('https://www.quora.com/unanswered/Who-is-the-gayest-straight-person-you-have-ever-met')

def login(): ##login to Quora --- not always necassary
    browser.get('http://www.quora.com')

    fields = browser.find_elements_by_class_name("text header_login_text_box ignore_interaction")  # selects the login text fields
    fields[0].send_keys(email)
    fields[1].send_keys(password)

    login = browser.find_element_by_class_name('submit_button ignore_interaction')
    login.click()  # logs in


def setting(): ##main function for requesting loop
    question_page()
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

def requesting(): ##controls each set of requests per question
    request = browser.find_elements_by_id('request') #Even though there is only one requets element will be present, array is returned so that it can be counted to determine whether request is present. Selenium does not allow to check for single element without returning error
    while len(request) == 0: #runs loop as long as request is still visible
        request = browser.find_elements_by_id('request')
        print('looking')
    print('found')
    request[0].click()
    print('clicked')
    submit = browser.find_elements_by_class_name('submit_button modal_action')
    while (len(submit) == 0):## make sure request screen is loaded
        request[0].click()
        submit = browser.find_elements_by_class_name('submit_button modal_action')
        print('click')
    #users = browser.find_elements_by_class_name('user')  # to look cool shows names and stuff
    no_requests_left = browser.find_elements_by_class_name('u-sans-font-main--large u-font-weight--bold u-margin-bottom--sm')
    if len(no_requests_left) != 0: ##if no more requests screen exists end requests
        return
    i = 0
    buttons = browser.find_elements_by_class_name('u-flex-none u-relative u-flex-align-self--center button_wrapper')
    while len(buttons) < 50 or i == 150:
        time.sleep(.01)
        buttons = browser.find_elements_by_class_name('u-flex-none u-relative u-flex-align-self--center button_wrapper')
    buttoncount = len(buttons)
    if buttoncount > 50:
        buttoncount = 50

    for x in range(0, buttoncount, 2):
        browser.execute_script("arguments[0].scrollIntoView(true);", buttons[(x)])
        buttons[x].click()  ##must be even for whatever reason
        global count
        count +=1
        print(str(count))


def submit():
    submit = browser.find_elements_by_class_name('submit_button modal_action')
    submit[2].click()

