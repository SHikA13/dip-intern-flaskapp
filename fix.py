import pandas as pd
import numpy as np
import pickle
from flask import Flask,request,render_template

def column():
    test_x = pd.read_csv("test_x.csv")
    col = test_x["お仕事No."]
    return col



def data_fix():
    
    test_x = pd.read_csv("test_x.csv")
    
    # 下処理
    
    del test_x["お仕事No."]
    test_x = test_x.dropna(how="all",axis=1)
    test_x = test_x.drop(['掲載期間　開始日','期間・時間　勤務開始日','掲載期間　終了日'],axis=1)
    del test_x["（紹介予定）雇用形態備考"]
    test_x["（紹介予定）入社後の雇用形態"] = test_x["（紹介予定）入社後の雇用形態"].fillna(0)
    list_0_1 = ["勤務地　最寄駅2（駅名）","勤務地　最寄駅2（沿線名）","（派遣先）勤務先写真ファイル名",
            "（派遣先）概要　事業内容","（派遣先）職場の雰囲気","（紹介予定）待遇・福利厚生","期間･時間　備考",
            "（派遣先）配属先部署","（派遣先）概要　勤務先名（漢字）"]
    for i in list_0_1:
        test_x.loc[~(test_x[i].isnull()),i] = 1
        test_x.loc[test_x[i].isnull(),i] = 0
    mean_list = ["（派遣先）配属先部署　男女比　男","（派遣先）配属先部署　人数","勤務地　最寄駅1（分）",
         "（派遣先）配属先部署　男女比　女","（派遣先）配属先部署　平均年齢","給与/交通費　給与上限",
         "勤務地　最寄駅1（駅からの交通手段）","勤務地　最寄駅2（分）"]
    for i in mean_list:
        test_x[i] = test_x[i].fillna(test_x[i].mean())
    num_list = ["（紹介予定）入社時期","（紹介予定）年収・給与例","（紹介予定）休日休暇","給与/交通費　備考"]
    for i in num_list:
        test_x[i] = test_x[i].str.extract("(\d+)")
        test_x[i] = test_x[i].fillna(0).astype(int)
    s_i_list = ["勤務地　最寄駅2（駅名）","勤務地　最寄駅2（沿線名）","（派遣先）概要　勤務先名（漢字）",
           "（派遣先）勤務先写真ファイル名","（派遣先）概要　事業内容","（派遣先）職場の雰囲気","期間･時間　備考"]
    for i in s_i_list:
        test_x[i] = test_x[i].astype(int)
    list_1 = ["休日休暇　備考","（派遣）応募後の流れ","期間・時間　勤務時間","勤務地　備考","お仕事名","（派遣先）配属先部署",
         "動画タイトル","勤務地　最寄駅1（沿線名）","応募資格","派遣会社のうれしい特典","お仕事のポイント（仕事PR）","動画ファイル名",
         "（紹介予定）待遇・福利厚生","勤務地　最寄駅1（駅名）","仕事内容","拠点番号","動画コメント"] 
    for i in list_1:
        test_x[i] = 1
    test_x["勤務地　最寄駅2（駅からの交通手段）"] = test_x["勤務地　最寄駅2（駅からの交通手段）"].fillna(0)
    


    return test_x