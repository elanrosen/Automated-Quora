from selenium import webdriver

email = 'surfer.zoke@gmail.com' ##inputs for account
password = 'Burrito1'
browser = webdriver.Chrome("chromedriver.exe") ##loads driver
browser.implicitly_wait(5)

def login():
    browser.get('http://www.quora.com')

    fields = browser.find_elements_by_class_name("text header_login_text_box ignore_interaction")  # selects the login text fields
    fields[0].send_keys(email)
    fields[1].send_keys(password)

    login = browser.find_element_by_class_name('submit_button ignore_interaction')
    login.click()  # logs in

def setting_up_request():
    browser.get('https://www.quora.com/profile/Tom-Pierre-1/questions')  # heads to question page

    questions = browser.find_elements_by_class_name('ui_content_title ui_content_title--default ui_content_title--medium')  ##array to store links
    profile_counts = browser.find_elements_by_class_name('list_count')
    question_count = int(profile_counts[1].text)
    for i in range(0, question_count):
        if i == 0:
            questions[i].click()
        else:
            questions = browser.find_elements_by_class_name('ui_content_title ui_content_title--default ui_content_title--medium')  ##adds new questions to list
            browser.execute_script("arguments[0].scrollIntoView(true);", questions[(i - 1)])
            questions = browser.find_elements_by_class_name('ui_content_title ui_content_title--default ui_content_title--medium')  ##adds new questions to list
            print(questions[i].text)
            questions[(i)].click()


        questionPage = browser.window_handles[1] ##changes browser tab
        browser.close()
        browser.switch_to.window(questionPage)

        request = browser.find_element_by_id('request')
        request.click()
        time.sleep(1)
        browser.get('https://www.quora.com/profile/Tom-Pierre-1/questions')  # heads to question page


def requesting():
    buttons = browser.find_elements_by_class_name('u-flex-none u-relative u-flex-align-self--center button_wrapper')
    users = browser.find_elements_by_class_name('user')  # to look cool shows names and stuff
    buttoncount = len(buttons)
    if buttoncount > 50:
        buttoncount = 50

    for x in range(0, buttoncount):
        browser.execute_script("arguments[0].scrollIntoView(true);", users[(x)])
        buttons[x].click()  ##must be even for whatever reason
        print('Requested ' + users[x].text)
        x += 2

def submit():
    submit = browser.find_elements_by_class_name('submit_button modal_action')
    submit[2].click()

login()
setting_up_request()
requesting()





