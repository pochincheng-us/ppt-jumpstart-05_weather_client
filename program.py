import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, cond, temp, scale')


def main():
    print_the_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print("The temp in {} is {} {} and {}.".format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

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
    # weatherConditionCss = '.condition-icon'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # print("loc = {}\ncondition = {}\ntemp = {}\nscale = {}".format(loc, condition, temp, scale))

    report = WeatherReport(loc=loc, cond=condition, temp=temp, scale=scale)
    return report

def find_city_and_state_from_location(loc : str):
    parts = loc.split('\n')
    return parts[0].strip()

def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text

if __name__ == '__main__':
    main()
