import requests
import json
import mysql.connector
from selenium import webdriver
import time
import traceback
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
try:
     config = {
     "user": "root",
     "password": "12345",
     "host": "localhost",
     "port": "3306",
     "database": "country_players",
     }
     conn = mysql.connector.connect(**config)
     if conn.is_connected():
          print("Connected")

     myc = conn.cursor()
     # coutries = ['afghanistan-40','australia-2','bangladesh-25','england-1','india-6','ireland-29','new-zealand-5','pakistan-7','south-africa-3','sri-lanka-8','west-indies-4','zimbabwe-9','namibia-28','nepal-33','netherlands-15','oman-37','papua-new-guinea-20','scotland-30','united-arab-emirates-27','united-states-of-america-11']
     coutries = ['afghanistan-40']
     for c in coutries:
          driver = webdriver.Chrome()
          url = f'https://www.espncricinfo.com/cricketers/team/{c}'
          driver.get(f'https://www.espncricinfo.com/cricketers/team/{c}')
          driver.maximize_window()
          total_height = int(driver.execute_script("return document.body.scrollHeight"))
          print(total_height)
     for i in range(1, 4000):
          driver.execute_script("window.scrollTo(0, {});".format(i))
          # time.sleep(0.001)

     soup =BeautifulSoup(driver.page_source, 'html.parser')
     main = []
     all_player = soup.find_all('div',class_="ds-flex ds-p-4 ds-flex-row ds-space-x-4 ds-border-line ds-border-b odd:ds-border-r last:ds-border-none")
     for player in all_player:
          player_full_name = player.find('span',class_="ds-text-tight-l").text
          player_age = player.find('span',class_="ds-text-tight-m ds-font-regular ds-text-typo-mid3").text.strip('Age:')
          # player_image = player.find('a',class_="ds-flex").find("img").get('src')44
          player_image = player.find('img').get('src')
          url = player.find('a').get('href')
          player_url = f'https://www.espncricinfo.com/{url}'
          r = requests.get(player_url)
          soup = BeautifulSoup(r.content,'html.parser')
          gender = soup.find('span',class_="ds-cursor-pointer ds-inline-flex ds-items-start ds-leading-none").text
          all_span = soup.find('div',class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8").text
          playing_role = None
          country_name=f'{c}'
          if "Bowler" in all_span:
               playing_role="Bowler"
          elif "Allrounder" in all_span:
               playing_role="Allrounder"
          else:
               playing_role="Batter"
          if "Women" in gender:
               gender = "female"
          else:
               gender = "Male"  
                     
          new_dict={
               'player_name':player_full_name,
               'player_age':player_age,
               'player_image':player_image,
               "Gender":gender,
               "Playing_role":playing_role,
               "player_country":country_name
               
          }
          # sql ='CREATE TABLE india_player(id INT AUTO_INCREMENT PRIMARY KEY,player_name varchar(255),player_age varchar(255),player_image varchar(255),gender varchar(255),playing_role varchar(255))'
          d =(player_full_name,player_age,player_image,gender,playing_role,country_name)
          sql = (f"INSERT INTO app_espncrici_player_info(player_name, player_age, player_image, player_gender, player_playing_role,player_country) VALUES ('%s','%s','%s','%s','%s','%s')"%d)
   
          myc.execute(sql)    
          conn.commit()
          # # myc.close()
          # conn.close()
          main.append(new_dict)
    
except Exception as e:
      print(f"Exception: {e}\n{traceback.format_exc()}")


    