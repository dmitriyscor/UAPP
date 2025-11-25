import csv_parser
import analysis

df = csv_parser.load_data()
user = csv_parser.load_user()

user_timestamp = csv_parser.get_user_timestamp(user)
print (user_timestamp)


extr = analysis.extr_act_stats(user, df)
print(extr)

atnd = analysis.class_atd(user, df)
print(atnd)
#  "0–60%":  0,
#  "60–80%": 1,
#  "80–90%": 2,
# "90–100%": 3

wkl_std_hr = analysis.weekly_study_hours_stats(user, df)
print(wkl_std_hr)

crs_ld = analysis.units_load_stats(user, df)
print(crs_ld)
#  "8-12 units": 0,
# "13-14 units": 1,
# "15-16 units": 2,
# "17-18 units": 3,
#   "19+ units": 4

ai_use = analysis.use_of_ai_distribution(user, df)
print("Categories:", ai_use["categories"])
print("Percentage distribution across all data:", ai_use["overall_percent"])
print("Percentage distribution by user:", ai_use["user_percent"])

slp_time = analysis.sleep_hours_stats(user, df)
print(slp_time)