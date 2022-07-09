import requests

def getPicture(birthday):
    bday_number = birthday
    # bday_number = '19800713'
    bday_year = bday_number[:4]
    int_bday = int(bday_year)

    if int_bday < 1996:
        birth_year = 2021
    else:
        birth_year = bday_year

    # birth_year = bday_number[:4]
    birth_month = bday_number[4:6]
    birth_day = bday_number[6:]


    response = requests.get(
        # "https://api.nasa.gov/planetary/apod?api_key=z6IDurSdstj9WmDioKM09GwIKI5LerBrWcyglKzJ&date=1996-04-15"
        f'https://api.nasa.gov/planetary/apod?api_key=z6IDurSdstj9WmDioKM09GwIKI5LerBrWcyglKzJ&date={birth_year}-{birth_month}-{birth_day}'
    )


    dic = response.json()

    if 'hdurl' in dic:
        print(dic['hdurl'])
    else:
        response = requests.get(
        "https://api.nasa.gov/planetary/apod?api_key=z6IDurSdstj9WmDioKM09GwIKI5LerBrWcyglKzJ&date=2021-12-25"   
        )
        dic = response.json()
        print(dic['hdurl'])
    return dic['hdurl']

# birthday_pic = dic['hdurl']
# print(dic['hdurl'])
# # print(response.text)

# dic
# bday_pic = request.get(hdul)

