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
    user_data = csv_parser.get_user_use_of_ai(user_df)

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
    user_data = csv_parser.get_user_sleep_hours(user_df)

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

# Major
def normalize_major(text: str) -> str:
    if not isinstance(text, str):
        return "other"
    s = text.strip().lower()

    # computer science / cs / robotics / cmdb-like
    if "computer science" in s or s == "cs" or "cs " in s or " robotics" in s:
        return "cs"
    if "data science" in s or "data science" == s:
        return "data_science"
    if "statistics" in s or "statistic" in s:
        return "statistics"
    if "math" in s or "mathematics" in s:
        return "math"

    # engineering
    if "engineering" in s:
        return "engineering"

    # business / economics / pre-business
    if "business" in s or "economics" in s or "pre-business" in s:
        return "business"

    # biology / chemistry / physics / neuroscience / bio
    if "biology" in s or "bio " in s or s == "bio" or "cmdb" in s:
        return "biology"
    if "chemistry" in s or "chemical" in s:
        return "chemistry"
    if "physics" in s:
        return "physics"
    if "neuroscience" in s:
        return "neuroscience"

    # psychology
    if "psychology" in s or s == "psych":
        return "psychology"

    # education / liberal studies
    if "education" in s or "liberal studies" in s:
        return "education"

    # theater / acting
    if "theater" in s or "acting" in s:
        return "arts"

    # anthropology / sociology / social science
    if "anthropology" in s or "sociology" in s:
        return "social_science"

    return "other"

def major_stats(user, df):
    data = csv_parser.get_major(df)
    user_data = csv_parser.get_user_major(user)

    majors_norm = [normalize_major(m) for m in data]
    user_majors_norm = [normalize_major(m) for m in user_data]

    total = len(majors_norm)
    counts = {}
    for m in majors_norm:
        counts[m] = counts.get(m, 0) + 1

    if total == 0:
        overall_percent = {}
    else:
        overall_percent = {m: (c / total) * 100 for m, c in counts.items()}

   
    user_major = user_majors_norm[0] if user_majors_norm else None

    return {
        "user_major": user_major,          
        "overall_percent": overall_percent 
    }

# Languages
def lang_stats(user, df):
    data = csv_parser.get_languages_spoken(df)
    user_data = csv_parser.get_user_languages_spoken(user)

    total = len(data)

    return {
        "user": user_data[0],
        "overall_percent": data
    }

# Water
def water_stats(user, df):
    categories = ["Less than 1 liter (about 3 cups)", "1–2 liters", "2–3 liters", "More than 3 liters"]
    
    data = csv_parser.get_water_consumption(df)
    user_data = csv_parser.get_user_water_consumption(user)

    def get_percentages(lst, categories):
        total = len(lst)
        if total == 0:
            return [0.0] * len(categories)
        
        counts = {cat: 0 for cat in categories}
        for val in lst:
            clean_val = str(val).strip()
            if clean_val in counts:
                counts[clean_val] += 1
        
        return [round((counts[cat] / total) * 100, 2) for cat in categories]

    overall_percent = get_percentages(data, categories)

    return {
        "categories": categories,
        "overall_percent": overall_percent,  
        "user_percent": user_data         
    }

# App
def app_stats(user, df):
    categories = ["None", "Paper planner", "Google Calendar", "Todoist or another task manager app", "Other"]
    
    data = csv_parser.get_organization(df)
    user_data = csv_parser.get_user_organization(user)

    def get_percentages(lst, categories):
        total = len(lst)
        if total == 0:
            return [0.0] * len(categories)
        
        counts = {cat: 0 for cat in categories}
        for val in lst:
            clean_val = str(val).strip()
            if clean_val in counts:
                counts[clean_val] += 1
        
        return [round((counts[cat] / total) * 100, 2) for cat in categories]

    overall_percent = get_percentages(data, categories)
    

    return {
        "categories": categories,
        "overall_percent": overall_percent,
        "user_option": user_data
    }

# School GPA
def gpa_stats(user, df):
    categories = ["2.0–2.7", "2.7–3.0", "3.0–3.3", "3.3–3.7", "3.7–4.0"]
    
    data = csv_parser.get_school_gpa(df)
    user_data = csv_parser.get_user_school_gpa(user)

    def get_percentages(lst, categories):
        total = len(lst)
        if total == 0:
            return [0.0] * len(categories)
        
        counts = {cat: 0 for cat in categories}
        for val in lst:
            clean_val = str(val).strip()
            if clean_val in counts:
                counts[clean_val] += 1
        
        return [round((counts[cat] / total) * 100, 2) for cat in categories]

    overall_percent = get_percentages(data, categories)
    user_percent = get_percentages(user_data, categories)

    return {
        "categories": categories,
        "overall_percent": overall_percent, 
        "user_percent": user_percent
    }



