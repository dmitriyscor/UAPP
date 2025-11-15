import csv_parser

df = csv_parser.load_data()


# Example
ai_usage = csv_parser.get_use_of_ai(df)
print(ai_usage)