#!/usr/bin/env python
#coding=utf8

import urllib
from tornado.web import RequestHandler
from lib  import session
from lib.mixin import FlashMessagesMixin
from model import Category, Distribution
import logging

class BaseHandler(RequestHandler, FlashMessagesMixin):

    def set_default_headers(self):
        self.clear_header('Server')

    def render_string(self, template_name, **context):
        context.update({
            'xsrf': self.xsrf_form_html,
            'module': self.ui.modules,
            'request': self.request,
            'user': self.current_user,
            'handler': self,}
        )

        return self._jinja_render(path = self.get_template_path(),filename = template_name,
            auto_reload = self.settings['debug'], **context)

    def _jinja_render(self,path,filename, **context):
        template = self.application.jinja_env.get_template(filename,parent=path)
        return template.render(**context)

    @property
    def is_xhr(self):
        return self.request.headers.get('X-Requested-With', '').lower() == 'xmlhttprequest'

    @property
    def session(self):
        if hasattr(self, '_session'):
            return self._session
        else:
            self._session  = session.Session(self.application.session_manager, self)

            return self._session

    def get_current_user(self):
        logging.info(self.session.get("user",None))
        return self.session.get("user",None)
    @property
    def next_url(self):
        return self.get_argument("next", "/")

    def get_categorys(self):
        categorys = self.session.get('categorys')

        if not categorys:
            categorys = [category for category in Category.select()]
            self.session.set('categorys', categorys, 86400)

        return categorys

    def get_distributions(self):
        distributions = self.session.get('distributions')

        if not distributions:
            distributions = {}

            for distribution in Distribution.select().dicts():
                if distribution['pdid'] == 0:
                    distribution['list'] = []
                    distributions[distribution['id']] = distribution
                else:
                    distributions[distribution['pdid']]['list'].append(distribution)

            self.session.replace('distributions', distributions, 86400)
        return distributions

class AdminBaseHandler(BaseHandler):

    def prepare(self):
        if not self.current_user:
            url = self.get_login_url()
            if "?" not in url:
                url += "?" + urllib.urlencode(dict(next=self.request.full_url()))
            self.redirect(url)
        elif self.current_user['group'] != 9:
            self.redirect("/")

        super(AdminBaseHandler, self).prepare()

class UserBaseHandler(BaseHandler):

    def prepare(self):
        if not self.current_user:
            url = self.get_login_url()
            if "?" not in url:
                url += "?" + urllib.urlencode(dict(next=self.request.full_url()))
            self.redirect(url)

        super(UserBaseHandler, self).prepare()