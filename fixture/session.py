__author__ = 'rmostafin'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.open_login_page()
        # fill auth form
        wd.find_element_by_id('exampleInputEmail1').send_keys(username)
        wd.find_element_by_id('exampleInputPassword1').send_keys(password)
        wd.find_element_by_name('_csrf').click()

    def logout(self):
        wd = self.app.wd
        # open dropdown menu
        wd.find_element_by_id('navbarDropdown2').click()
        # select "logout"
        wd.find_element_by_css_selector('[class="dropdown-menu show"]') \
            .find_elements_by_css_selector('a')[2].click()

    def ensure_logout(self):
        if len(self.is_logged_in()) > 0:
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return wd.find_elements_by_id('navbarDropdown2')

    def is_logged_in_as(self, name):
        wd = self.app.wd
        return wd.find_element_by_css_selector('[id="navbarDropdown2"]').text.strip() == name

    def ensure_login(self, username, password, name):
        if self.is_logged_in():
            if self.is_logged_in_as(name):
                return
            else:
                self.logout()
        self.login(username, password)


