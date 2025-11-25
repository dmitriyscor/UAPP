import csv_parser
import numpy as np



#   Extracurricular Activities      [user_data, mean, median, std] ; 0 <= user_value <= 32+
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

# Class Attendance              [user_data, mean, median, std] ; 0 <= user_value <= 3
def class_atd(user, df):
    mapping = {
        "0–60%": 0,
        "60–80%": 1,
        "80–90%": 2,
        "90–100%": 3
    }

    df_attendance = csv_parser.get_class_attendance(df)
    user_attendance = csv_parser.get_user_class_attendance(user)

    def map_to_numeric(cat_list):
        result = []
        for val in cat_list:
            result.append(mapping.get(val.strip(), None))  # None for unknown numbers
        return result

    df_numeric = map_to_numeric(df_attendance)
    user_numeric = map_to_numeric(user_attendance)
    user_value = user_numeric[0] if user_numeric and user_numeric[0] is not None else None

    df_clean = [x for x in df_numeric if x is not None]

    mean = np.mean(df_clean) if df_clean else None
    median = np.median(df_clean) if df_clean else None
    std = np.std(df_clean) if df_clean else None

    return [user_value, mean, median, std]


# Weekly Study Hours        [user_value, mean, median, std] ; 3 <= user_value <= 25 
def weekly_study_hours_stats(user, df): 
    mapping = {
        "0-5": 3,
        "6-10": 8,
        "11-15": 13,
        "16-20": 18,
        "21+": 25
    }

    df_hours = csv_parser.get_weekly_study_hours(df)
    user_hours = csv_parser.get_user_weekly_study_hours(user)

    def map_to_numeric(cat_list):
        result = []
        for val in cat_list:
            v = val.strip()
            v = v.replace(" ", "")
            result.append(mapping.get(v, None))
        return result

    df_numeric = map_to_numeric(df_hours)
    user_numeric = map_to_numeric(user_hours)
    user_value = user_numeric[0] if user_numeric and user_numeric[0] is not None else None

    df_clean = [x for x in df_numeric if x is not None]

    mean = np.mean(df_clean) if df_clean else None
    median = np.median(df_clean) if df_clean else None
    std = np.std(df_clean) if df_clean else None

    return [user_value, mean, median, std]

# Units Load
def units_load_stats(user, df):     # [user_value, mean, median, std] ; 0 <= user_value <= 4
    mapping = {
        "8-12 units": 0,
        "13-14 units": 1,
        "15-16 units": 2,
        "17-18 units": 3,
        "19+ units": 4
    }

    df_units = csv_parser.get_course_load(df)
    user_units = csv_parser.get_user_course_load(user)

    def map_to_numeric(cat_list):
        result = []
        for val in cat_list:
            result.append(mapping.get(val.strip(), None))  # None for unknown numbers
        return result
    
    df_numeric = map_to_numeric(df_units)
    user_numeric = map_to_numeric(user_units)
    user_value = user_numeric[0] if user_numeric and user_numeric[0] is not None else None

    df_clean = [x for x in df_numeric if x is not None]

    mean = np.mean(df_clean) if df_clean else None
    median = np.median(df_clean) if df_clean else None
    std = np.std(df_clean) if df_clean else None

    return [user_value, mean, median, std]

# AI use
def use_of_ai_distribution(user_df, df):
    data = csv_parser.get_use_of_ai(df)
    user_data = csv_parser.get_use_of_ai(user_df)

    categories = [
        "I don't use AI",
        "I consult AI for guidance on homework questions",
        "I use AI as an assistant to my studying efforts"
    ]

    def get_percentages(lst):
        total = len(lst)
        counts = {cat: 0 for cat in categories}
        for val in lst:
            val = val.strip()
            if val in counts:
                counts[val] += 1
        if total == 0:
            return {cat: 0 for cat in categories}
        return {cat: (counts[cat] / total) * 100 for cat in categories}

    overall_percent = get_percentages(data)
    user_percent = get_percentages(user_data)

    return {
        "categories": categories,
        "overall_percent": overall_percent,
        "user_percent": user_percent
    }


# Sleep Hours
def sleep_hours_stats(user_df, df):     # [user_value, mean, median, std] ; 0 <= user_value <= 10+
    data = csv_parser.get_sleep_hours(df)
    user_data = csv_parser.get_sleep_hours(user_df)

    def to_float_list(lst):
        result = []
        for x in lst:
            try:
                result.append(float(x))
            except (ValueError, TypeError):
                continue
        return result

    data_numeric = to_float_list(data)
    user_numeric = to_float_list(user_data)

    user_value = user_numeric[0] if user_numeric else None

    mean = np.mean(data_numeric) if data_numeric else None
    median = np.median(data_numeric) if data_numeric else None
    std = np.std(data_numeric) if data_numeric else None

    return [user_value, mean, median, std]



