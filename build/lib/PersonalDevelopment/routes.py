def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('main_page', '/')
    config.add_route('user_main', '/user_main')
    config.add_route('registration', '/registration')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('statistics', '/statistics')
    config.add_route('radar_example', '/radar_example')
    config.add_route('delete_user_data', '/delete_user_data')
    config.add_route('check_db', '/check_db')
