import csv
import pprint
from collections import Counter

def generate_report():
    '''
    Generate a report based on the data from the CSV file.
    Returns:
        dict: A dictionary containing the report data. The keys are:
            - 'dev_activities': A dictionary containing the count of developers based on their activity.
            - 'most_used_language': A dictionary containing the count of developers based on the most used language.
            - 'most_wanted_language': A dictionary containing the count of developers based on the most wanted language.
            - 'most_used_framework': A dictionary containing the count of developers based on the most used framework.
            - 'most_wanted_framework': A dictionary containing the count of developers based on the most wanted framework.
            - 'most_used_tool': A dictionary containing the count of developers based on the most used tool.
            - 'most_wanted_tool': A dictionary containing the count of developers based on the most wanted tool.
            - 'most_personal_operating_system': A dictionary containing the count of developers based on the most used operating system.
            - 'most_professional_operating_system': A dictionary containing the count of developers based on the most wanted operating system.
            - 'popular_industry': A dictionary containing the count of developers based on the top three industries they work in.
    '''
    def read(num):
        with open('stackoverflow_survey.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            data = [row[num].split(";") for row in reader]
            res = [items for row in data for items in row if items != "NA"]
            value = Counter(res).most_common(3)
            return dict(value)
    result = {
        'dev_activities': read(0),
        'most_used_language': read(1),
        'most_wanted_language': read(2),
        'most_used_framework': read(3),
        'most_wanted_framework': read(4),
        'most_used_tool': read(5),
        'most_wanted_tool': read(6),
        'most_personal_operating_system': read(7),
        'most_professional_operating_system': read(8),
        'popular_industry': read(9)
    }
    return result

print(generate_report())