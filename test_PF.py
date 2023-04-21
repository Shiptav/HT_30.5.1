
import pytest
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def test_show_all_pets_explicit():
   pytest.driver = webdriver.Chrome('C:/Users/Antony/OneDrive/Desktop/QAP/LS30/driver/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('tttesttt@mail.ru')
   time.sleep(2)#явные ожидания
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('tttesttt')
   time.sleep(2)#явные ожидания
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   time.sleep(2)

   # try:
   # pets_img= WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))) #явные ожидания
   # assert pets_img.text=="PetFriends"
   assert WebDriverWait(pytest.driver, 10).until(EC.title_is("PetFriends: My Pets"))#явные ожидания
   
   # finally:
   pytest.driver.quit()



def test_show_all_pets_implicit():
   pytest.driver = webdriver.Chrome('C:/Users/Antony/OneDrive/Desktop/QAP/LS30/driver/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   insert_email=pytest.driver.find_element(By.ID,'email')
   insert_email.send_keys('tttesttt@mail.ru')
   #time.sleep(2)
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('tttesttt')
  
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   
   pytest.driver.quit()



def test_show_all_pets_task():
      
   pytest.driver = webdriver.Chrome('C:/Users/Antony/OneDrive/Desktop/QAP/LS30/driver/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('tttesttt@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('tttesttt')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
         
         
   pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
   time.sleep(2)
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "tttesttt"
      
   images= pytest.driver.find_elements(By.CSS_SELECTOR, 'img')
         
   # Проверяем колличество питомцев и фото, тут все питомцы с фото будут , видимо так сделан сайт
   list_pets_friends_mess=pytest.driver.find_element(By.CSS_SELECTOR, 'div[class=".col-sm-4 left').text
   num_pets = list_pets_friends_mess.split('\n') # сделали строку
   pets=num_pets[1] # вытащили питомцев
   quantity_pet=int(pets[9:]) # вытащили число питомцев
   quantity_images = int(len(images)) 
   assert quantity_pet == quantity_images-1 # колличесвто фото равно колличеству питомцев -1 , одна картинка лишняя в добавлении питомца 
   print(quantity_pet)
   print(len(images))
   # Проверяем колличество питомцев равное колличеству строк в таблице
   row_pets_table=pytest.driver.find_elements(By.CSS_SELECTOR, 'th[scope=row]')
   pets_number=int(len(row_pets_table))
   assert quantity_pet==pets_number
   pytest.driver.quit()

   
   
   
   
   
# #    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
# #    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
# #    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
# #    print(names)
# #    print("hello")

# #    for i in range(len(names)):
# #         # assert images[i].get_attribute('src') != '' #проверки существования фотографии в карточке мы просто проверяем, что путь, указанный в атрибуте src, не пустой.
# #         assert names[i].text != ''
# #         assert descriptions[i].text != ''
# #         assert ', ' in descriptions[i]
# #         parts = descriptions[i].text.split(", ")
# #         assert len(parts[0]) > 0
# #         assert len(parts[1]) > 0 
   