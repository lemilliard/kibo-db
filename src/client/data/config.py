def get_page_name(page_name):
    return data['base_page_name'] + ' - ' + page_name


def switch_night_mode():
    data['night_mode'] = not data['night_mode']
    return 'OK'


data = {
    'base_page_name': 'ManoucheQL',
    'main_menu': [
        {'name': 'Home', 'path': '/home'},
        {'name': 'Test', 'path': '/sub/test'}
    ],
    'night_mode': False,
    'current_page': ''
}

methods = {
    'get_page_name': get_page_name
}
