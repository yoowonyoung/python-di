import os
from datetime import datetime, timedelta

import yaml


class KnoxConstant:
    DEPARTMENT_NAME = 'deptname'
    DEPARTMENT_CODE = 'deptcode'
    DEPARTMENT_ORDER = 'order'
    UPPER_DEPARTMENT_CODE = 'upper_deptcode'
    GBM = 'gbm'
    TOP_GBM = '경영지원실'


class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)


def prev_month(when: datetime = datetime.today()):
    return datetime(day=1, month=when.month, year=when.year) - timedelta(days=1)


def get_yyyymm_string_from_year_and_month_string(year: int, month: int, delta: int = 0) -> str:
    when = datetime(year, month, 1)
    for _ in range(delta):
        when = prev_month(when)
    return when.strftime('%Y%m')


def get_yyyymm_string_from_datetime(date: datetime) -> str:
    return date.strftime('%Y%m')


def load_yaml(filename: str):
    res = None
    with open(filename, 'r') as f:
        res = yaml.load(f, Loader=Loader)
    return res
