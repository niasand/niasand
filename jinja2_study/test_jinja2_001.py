# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by ZhiWei Yang
# Create At: 2023/12/10 22:54

from jinja2 import Template
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('yourapplication', 'templates'))


def test_001():
    template = Template("Hello {{ name }}")
    template.render(name="John Doe")