import pandas as pd

# Survey Data

def load_data(filepath="data/Academic Habits and Rules Survey.csv"):
    return pd.read_csv(filepath)
    pass

def get_extracurricular_activities(df):
    return df["On average, how much time do you spend participating in extracurricular activities?"].to_list()

def get_class_attendance(df):
    return df["How many of your class meetings do you attend in a typical week?"].to_list()

def get_weekly_study_hours(df):
    return df["Weekly study hours"].to_list()

def get_course_load(df):
    return df["Course load"].to_list()

def get_use_of_ai(df):
    return df["How would you describe your use of AI tools (ChatGPT, Gemini, Claude)?"].to_list()

def get_sleep_hours(df):
    return df["On average, how many hours of sleep do you get per night?"].to_list()

def get_major(df):
    return df["What is your current major?"].to_list()

def get_languages_spoken(df):
    return df["How many languages do you speak fluently?"].to_list()

def get_water_consumption(df):
    return df["How much water do you drink daily on average?"].to_list()

def get_organization(df):
    return df["How do you usually organize or remember your schedule?"].to_list()

def get_school_gpa(df):
    return df["What was your high school GPA?"].to_list()

def get_college_gpa(df):
    return df["And finally, what is your college GPA?"].to_list()


# User Data




