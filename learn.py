import pandas as pd
import pickle
import fix
import io

def machine_learn():

    fix.column()
    fix.data_fix()
        
    col = fix.column()
    test_x =fix.data_fix()
        
    # 保存したモデルで予測
        
        
    loaded_model = pickle.load(open('saved_model','rb'))
    answer = pd.DataFrame(loaded_model.predict(test_x))
        
    answer["お仕事No."] = col
    answer[["お仕事No.","応募数 合計"]] = answer[["お仕事No.",0]]
    answer = answer.drop(0,axis=1)
        
    buffer = io.StringIO()
    answer.to_csv(buffer,index=False)

    return buffer
    

    