from mysql.connector import connect as ConnectDB
import requests
import json
from bs4 import BeautifulSoup
import traceback

try:
# database connection
    config = {
    "user": "root",
    "password": "12345",
    "host": "localhost",
    "port": "3306",
    "database": "ICC_TOP_RANKING"
    }
    conn = ConnectDB(**config)    
    if conn.is_connected():
        print("Connected")
    myc = conn.cursor(buffered=True)
    

    gender= {'men':'male','women':'female'}
    playing_style={'batting':'batsmen','bowling':'bowlers','all-rounder':'allrounders'}
    
    for gender_k, gender_v in gender.items():
        for style_k, style_v in playing_style.items():
            # print(f"strting for {style_k}")
            url = f"https://www.cricbuzz.com/cricket-stats/icc-rankings/{gender_k}/{style_k}"
            print(url)
            r = requests.get(url)
            if r.status_code == 200:
                print("request successful")
            else:
                print("request failed")

            soup = BeautifulSoup(r.content, "html.parser")
            
            series_dict={}
        
            test = soup.find("div",attrs={"ng-show":f"'{style_v}-tests' == act_rank_format"})# 'bowlers-tests' 'allrounders-tests'
            if test:
                series_dict["test"]=test
                
            odi = soup.find("div",attrs={"ng-show":f"'{style_v}-odis' == act_rank_format"})
            if odi:
                series_dict["odi"]=odi
                
            t20 = soup.find("div",attrs={"ng-show":f"'{style_v}-t20s' == act_rank_format"})
            if t20:
                series_dict["t20"]=t20
        
            for key,value in series_dict.items():            
                player_row = value.find_all("div", class_="cb-col cb-col-100 cb-font-14 cb-lst-itm text-center")
                
                # player_info      
                for player in player_row:
                    image_url = player.find("img", class_="img-responsive cb-rank-plyr-img").get(
                        "src"
                    )
                    image = f"https://www.cricbuzz.com/{image_url}"
                    name = player.find(
                        "a", class_="text-hvr-underline text-bold cb-font-16"
                    ).text
                    coutry = player.find("div", class_="cb-font-12 text-gray").text
                    position = player.find("div", class_="cb-col cb-col-16 cb-rank-tbl cb-font-16").text
                    rating = player.find("div", class_="cb-col cb-col-17 cb-rank-tbl pull-right").text
                    

                    myc.execute(f"SELECT * FROM app_player_info WHERE name='{name}'")
                    existing_player = myc.fetchone()
                    # print(existing_player)
                    if existing_player==None:
                        d = (image, name, coutry, gender_v)
                        sql = (f"INSERT INTO app_player_info(image, name, country, gender) VALUES ('%s', '%s', '%s', '%s')"%d) 
                        myc.execute(sql)
                        player_id = myc.lastrowid
                        
                    else:
                        player_id=existing_player[0]
                    
                    # icc_bowling  , icc_batting,      
                    d = (position, rating, key, player_id)       
                    sql = (f"INSERT INTO app_icc_{style_k.replace('-','_')}(position, rating, series, player_id) VALUES ('%s','%s', '%s', '%s')"%d) 
                    myc.execute(sql)
                    
    conn.commit()
    conn.close()
                    # player_id = myc.lastrowid
   
except Exception as e:
    print(f"Exception: {e}\n{traceback.format_exc()}")
        
        
