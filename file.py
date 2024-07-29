import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

table_plans = []


def get_file():
    url = 'https://uust.ru/sveden/education/educational-programs/2024/'
    response = requests.get(url)
    soup = bs(response.content, 'html5lib')

    table = soup.find('table')

    for row in table.findAll('tr', attrs={'itemprop': 'eduOp'}):
        tds = row.findAll('td')
        plans = {
            'eduCode': row.find('td', attrs={'itemprop': 'eduCode'}).text.strip() if row.find('td', attrs={
                'itemprop': 'eduCode'}) else 'N/A',
            'eduName': row.find('td', attrs={'itemprop': 'eduName'}).text.strip() if row.find('td', attrs={
                'itemprop': 'eduName'}) else 'N/A',
            'eduProf': row.find('td', attrs={'itemprop': 'eduProf'}).text.strip() if row.find('td', attrs={
                'itemprop': 'eduProf'}) else 'N/A',
            'department': tds[4].text.strip() if len(tds) > 4 else 'N/A',
            'eduLevel': row.find('td', attrs={'itemprop': 'eduLevel'}).text.strip() if row.find('td', attrs={
                'itemprop': 'eduLevel'}) else 'N/A',
            'eduForm': row.find('td', attrs={'itemprop': 'eduForm'}).text.strip() if row.find('td', attrs={
                'itemprop': 'eduForm'}) else 'N/A',
            'educationPlan': row.find('td', attrs={'itemprop': 'educationPlan'}).find('a')['href'] if row.find('td',
                                    attrs={'itemprop': 'educationPlan'}) and row.find(
                'td', attrs={'itemprop': 'educationPlan'}).find('a') else 'N/A'
        }
        table_plans.append(plans)


def save_to_excel(file_name='table_plans.xlsx'):
    df = pd.DataFrame(table_plans)
    df.to_excel(file_name, index=False)


def print_table_plans():
    for plan in table_plans:
        print(plan)


# Execute the functions
get_file()
print_table_plans()
save_to_excel()
'''

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

table_plans = []


def get_file():
    url = 'https://uust.ru/sveden/education/educational-programs/2024'
    response = requests.get(url)
    soup = bs(response.content, 'html5lib')

    table = soup.find('table')

    for row in table.findAll('tr', attrs={'itemprop': 'eduOp'}):
        tds = row.findAll('td')
        plans = {
            'eduCode': tds[0].text.strip() if len(tds) > 0 else 'N/A',
            'eduName': tds[1].text.strip() if len(tds) > 1 else 'N/A',
            'eduProf': tds[2].text.strip() if len(tds) > 2 else 'N/A',
            'department': tds[3].text.strip() if len(tds) > 3 else 'N/A',
            'eduLevel': tds[4].text.strip() if len(tds) > 4 else 'N/A',
            'eduForm': tds[5].text.strip() if len(tds) > 5 else 'N/A',
            'educationPlan': row.find('td', attrs={'itemprop': 'educationPlan'}).find('a')['href'] if row.find('td',
                                                                                                               attrs={
                                                                                                                   'itemprop': 'educationPlan'}) and row.find(
                'td', attrs={'itemprop': 'educationPlan'}).find('a') else 'N/A'
        }
        table_plans.append(plans)


def save_to_excel(file_name='table_plans.xlsx'):
    df = pd.DataFrame(table_plans)
    df.to_excel(file_name, index=False)


def print_table_plans():
    for plan in table_plans:
        print(plan)


# Выполнение функций
get_file()
print_table_plans()
save_to_excel()



def search_plan(query):
    results = [plan for plan in table_plans if
               query.lower() in plan['eduCode'].lower() or query.lower() in plan['eduName'].lower()]
    return results


if __name__ == "__main__":
    get_file()

    results = search_plan(query)

    if results:
        for plan in results:
            print("Код специальности: ", plan['eduCode'])
            print("Название специальности: ", plan['eduName'])
            print("Профиль: ", plan['eduProf'])
            print("Уровень образования: ", plan['eduLevel'])
            print("Форма обучения: ", plan['eduForm'])
            print("План обучения: ", plan['educationPlan'])
            print()
    else:
        print("Специальность не найдена.")'''

