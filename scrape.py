from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
from selenium.webdriver.chrome.options import Options
import pyperclip
import marg
from marg import merge_im

# options = Options()
# options.headless = True # Сховане відкриття браузера
driver = webdriver.Chrome(executable_path=binary_path)
deck_code = []

def first_five():
    driver.get("http://hsreplay.net/meta/")
    driver.implicitly_wait(30)  # Очікування щоб сторінка прогрузилась
        # Скрейп данних про топ колоди і засовування їх в список(проц вигршу, Назв колоди, ссилка на інф про колоду)
    ar_data = driver.find_elements_by_class_name('archetype-data')
    ar_name = driver.find_elements_by_class_name('archetype-name')
    ar_link = driver.find_elements_by_xpath("//*[contains(text(), 'Самая популярная колода')]")
    ar_data = [i.text for i in ar_data]
    ar_name = [i.text for i in ar_name]
    ar_link = [i.get_attribute("href") for i in ar_link]
    y = list(zip(ar_data, ar_name, ar_link))
    y = y[:5]
    return y



def deck_list(link):
    #Витягування коду колоди
    driver.get(link)
    driver.implicitly_wait(30)
    python_button = driver.find_element_by_xpath("/html/body/div[3]/div/aside/div[2]/div/span")
    python_button.click()
    data = pyperclip.paste()
    deck_code.append(data)


    # Знайти колоду, зпарсити всі міні зображення
    driver.get("https://www.yaytears.com/deck")
    inputelement = driver.find_element_by_id("deck")
    inputelement.send_keys(data)
    python_button = driver.find_element_by_xpath("//*[@id='root']/div/main/div/button")
    python_button.click()

    mini_img = driver.find_elements_by_xpath("//*[@id='root']/div/main/div/div[3]/div/div/div/ul/li/div/div/div/img")
    mini_img = [i.get_attribute("src") for i in mini_img]
    mini_img = mini_img[0::2]
    return mini_img

#
# def deck_inf(data):
#     # Парс коду колоди в задовільний вигляд
#     check_point = 0
#     for p in data:
#         p = list(p)
#         p =
#
#     return data



y = first_five()
z = list()
for i in range(len(y)):
    z.append(deck_list(y[i][2]))
print(z)
# deck_code = deck_inf(deck_code)
# print(deck_code)
driver.quit()
for i in range(len(z)):
    merge_im(z[i], i)




