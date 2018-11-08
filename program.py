
def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')

    # get html from web
    get_html_from_web(code)
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
    requests(url)

if __name__ == '__main__':
    main()
