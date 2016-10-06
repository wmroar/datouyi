# -*- coding:utf-8 -*-


class DataFormatBase(object):

    def __init__(self,origins,keyword):
        self.origins = origins
        self.keyword = keyword

    def get_format_data(self):
        pass

    def get_tables_data(self):
        pass

    def get_treadline_data(self):
        pass

    def get_map_data(self):
        pass
