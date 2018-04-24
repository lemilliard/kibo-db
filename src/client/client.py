from flask import render_template
import importlib
import importlib.util


def client_endpoint(p_page=None):
    if p_page is None:
        page = 'home.html'
    else:
        page = p_page + '.html'
    base_data = get_data('base')
    header_data = get_data('header')
    footer_data = get_data('footer')
    page_data = get_data(p_page)
    data = dict()
    if base_data is not False:
        data['base'] = base_data
    if header_data is not False:
        data['header'] = header_data
    if footer_data is not False:
        data['footer'] = footer_data
    if page_data is not False:
        data['page'] = page_data
    return render_template('base.html', page=page, data=data)


def get_data(p_page=None):
    if p_page is not None:
        module_name = p_page.replace('/', '.')
        module_name = '.' + module_name
        if importlib.util.find_spec(module_name, 'src.client.data'):
            return importlib.import_module(module_name, 'src.client.data')
    return False
