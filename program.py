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

    soup = bs4.BeautifulSoup(html, 'html5lib')
    loc = soup.find_all("div", class_='region-content-header')
    print(loc)


if __name__ == '__main__':
    main()
