import csv_parser
import analysis

df = csv_parser.load_data()
user = csv_parser.load_user()

# Example
#ai_usage = csv_parser.get_use_of_ai(df)
#print(ai_usage)


user_timestamp = csv_parser.get_user_timestamp(user)
print (user_timestamp)

result = analysis.extr_act_stats(user, df)
print(result)
