import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定数の定義
xpath  = '//*[@id="contents_liquid"]/table/tbody/'
url1 = 'https://db.netkeiba.com/race/'
csv_path = '/Users/sasakiaoto/Downloads/競馬予想AI/data/data_15.csv'


# 1データのスクレイピング
browser = webdriver.Chrome()

def getMatrix(code,race):
  browser.get(f'{url1}{code}{race}/')
  # 着順,タイム,単勝倍率の取得
  txt_1 = browser.find_elements(By.CLASS_NAME,'txt_r')
  del txt_1[25:]
  text_1 = []
  for r in range(len(txt_1)):
    text_1.append(txt_1[r].text)
  array_1 = np.array(text_1).reshape((5,5))                      # 5行5列に変換
  list_1  = array_1.tolist()                                    # 行列(ndarray)は.textを使えないから一旦リストに変換する
  list_1 = np.delete(list_1,[1,4],1)
  # print(np.array(list_1).shape)                               # (5,3)
  # print(list_1[0][3].text)                                    # .textを適用するにはリスト型の1つの要素を指定する必要がある
  
  # 年齢,斤量の取得
  txt_2 = browser.find_elements(By.CLASS_NAME,'txt_c')
  del txt_2[31:]
  del txt_2[0]
  text_2 = []
  for c in range(len(txt_2)):
    text_2.append(txt_2[c].text)
  array_2 = np.array(text_2).reshape((5,6))
  list_2  = array_2.tolist()
  list_2  = np.delete(list_2,[2,3,4,5],1)
  # print(np.array(list_2).shape)                               # (5,2)
  # print(list_2[0][1].text)
  
  # 枠順の取得
  array_xpath = []
  txt_3 = []
  text_3 = []
  list_3 = []
  for i in range(2,7):
    array_xpath.append(f'{xpath}tr[{i}]/td[2]')
  for i in range(len(array_xpath)):
    txt_3.append(browser.find_element(By.XPATH,array_xpath[i]))
  for x in range(len(txt_3)):
    text_3.append(txt_3[x].text)
  list_3 = text_3
  # print(np.array(list_3).shape)                               # (5,1)

  # 馬体重の取得
  array_xpath = []
  txt_4 = []
  text_4 = []
  list_4 = []
  for i in range(2,7):
    array_xpath.append(f'{xpath}tr[{i}]/td[15]')
  for i in range(len(array_xpath)):
    txt_4.append(browser.find_element(By.XPATH,array_xpath[i]))
  for x in range(len(txt_4)):
    text_4.append(txt_4[x].text)
  list_4 = text_4
  # print(np.array(list_4).shape)                               # (5,1)
  
  # 行列の連結
  # print(type(list_1))                                          # ndarray
  # print(type(list_2))                                          # ndarray
  list_1 = np.transpose(list_1).tolist()
  list_2 = np.transpose(list_2).tolist()
  list_3 = np.array(list_3).reshape(1,-1)
  list_4 = np.array(list_4).reshape(1,-1)
  # print(list_3.shape)                                          # (1,5)
  list_3 = list_3.tolist()
  list_4 = list_4.tolist()
  list_1.extend(list_2)
  list_1.extend(list_3)
  list_1.extend(list_4)
  list_1 = np.transpose(list_1).tolist()
  # print(np.array(list_1).shape)                                # (5,7) 1列目:着順 , 2列目:タイム , 3列目:単勝倍率 , 4列目:年齢 , 5列目:斤量 , 6列目:枠順 , 7列目:馬体重
  matrix.extend(list_1)
  return matrix



# 全データのスクレイピング
# 回,日目の配列の定義
matrix = []
#others = ['2018090101', '2018090102', '2018090103', '2018090104', '2018090105', '2018090106', '2018090107', '2018090108']
#others = ['2018090201', '2018090202', '2018090203', '2018090204', '2018090205', '2018090206', '2018090207', '2018090208','2018090301', '2018090302', '2018090303', '2018090304', '2018090305', '2018090306', '2018090307', '2018090308']
#others = ['2018090401', '2018090402', '2018090403', '2018090404', '2018090405', '2018090406', '2018090407', '2018090408','2018090409']
#others = ['2018090501', '2018090502', '2018090503', '2018090504', '2018090505', '2018090506', '2018090507', '2018090508','2018090509','2021090101', '2021090102', '2021090103', '2021090104', '2021090105', '2021090106', '2021090107', '2021090108', '2021090109', '2021090110', '2021090111', '2021090112']
#others = ['2021090201', '2021090202', '2021090203', '2021090204', '2021090205', '2021090206', '2021090207', '2021090208', '2021090209', '2021090210', '2021090211', '2021090212','2021090301', '2021090302', '2021090303', '2021090304', '2021090401', '2021090402', '2021090403', '2021090404', '2021090405', '2021090406', '2021090407', '2021090408']
#others = ['2021090501', '2021090502', '2021090503', '2021090504', '2021090505', '2021090506', '2021090507', '2021090508','2021090601', '2021090602', '2021090603', '2021090604', '2021090605', '2021090606', '2021090607', '2021090608', '2021090609']
#others = ['2019090101', '2019090102', '2019090103', '2019090104', '2019090105', '2019090106', '2019090107', '2019090108','2019090201', '2019090202', '2019090203', '2019090204', '2019090205', '2019090206', '2019090207', '2019090208']
#others = ['2019090301', '2019090302', '2019090303', '2019090304', '2019090305', '2019090306', '2019090307', '2019090308','2019090401', '2019090402', '2019090403', '2019090404', '2019090405', '2019090406', '2019090407', '2019090408', '2019090409']
#others = ['2019090501', '2019090502', '2019090503', '2019090504', '2019090505', '2019090506', '2019090507', '2019090508','2019090509','2020090101', '2020090102', '2020090103', '2020090104', '2020090105', '2020090106', '2020090107', '2020090108', '2020090109']
#others = ['2020090201', '2020090202', '2020090203', '2020090204', '2020090205', '2020090206', '2020090207', '2020090208','2020090301', '2020090302', '2020090303', '2020090304', '2020090305', '2020090306', '2020090307', '2020090308']
#others = ['2020090401', '2020090402', '2020090403', '2020090404', '2020090405', '2020090406', '2020090501', '2020090502','2020090503', '2020090504', '2020090505', '2020090506', '2020090507', '2020090508', '2020090509']
#others = ['2020090601', '2020090602', '2020090603', '2020090604', '2020090605', '2020090606', '2020090607', '2020090608','2022090101', '2022090102', '2022090103', '2022090104', '2022090105', '2022090106', '2022090107', '2022090108', '2022090109', '2022090110', '2022090111', '2022090112']
#others = ['2022090201', '2022090202', '2022090203', '2022090204', '2022090205', '2022090206', '2022090207', '2022090208','2022090209', '2022090210', '2022090211', '2022090212', '2022090301', '2022090302', '2022090303', '2022090304', '2022090401', '2022090402', '2022090403', '2022090404', '2022090405', '2022090406', '2022090407', '2022090408', '2022090409']
#others = ['2022090501', '2022090502', '2022090503', '2022090504', '2022090505', '2022090506', '2022090507', '2022090508','2022090601', '2022090602', '2022090603', '2022090604', '2022090605', '2022090606', '2022090607', '2022090608', '2022090609']

# 過去5年間の阪神競馬場のデータの取得
for code in others:
  for i in range(1,13):
    race = str(i).zfill(2)
    getMatrix(code,race)
print(np.array(matrix).shape)

# csvに出力
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(matrix)