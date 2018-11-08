import bs4
import requests



def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')

    html = get_html_from_web(code)

    get_weather_from_html(html)
    # parse the html
    # display for the forecast

def print_the_header():
    app_name = 'WEATHER APP'
    dashes = '-' * (5 + len(app_name) + 5)
    spaces = ' ' * 5
    print("{}".format(dashes))
    print("{}{}{}".format(spaces, app_name, spaces))
    print("{}".format(dashes))
    print('')

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text

def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    print("loc = {}\ncondition = {}\ntemp = {}\nscale = {}".format(loc, condition, temp, scale))



if __name__ == '__main__':
    main()
