import csv_parser
import numpy as np



#   Extracurricular Activities [user_data, mean, median, std]
def extr_act_stats(user, df):
    df_ext = csv_parser.get_extracurricular_activities(df)
    user_ext = csv_parser.get_user_extracurricular_activities(user)

    def to_float_list(data_list):
        result = []
        for x in data_list:
            try:
                result.append(float(x))
            except ValueError:
                continue
        return result
    
    df_ext_numeric = to_float_list(df_ext)
    user_ext_numeric = to_float_list(user_ext)

    mean = np.mean(df_ext_numeric)
    median = np.median(df_ext_numeric)
    std = np.std(df_ext_numeric)

    user_value = user_ext_numeric[0] if user_ext_numeric else None

    return [user_value, mean, median, std]

# 


