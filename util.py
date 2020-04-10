#!/usr/bin/env python
# encoding: utf-8

import os
import random

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
try:
    install_folder = os.path.abspath(os.path.split(__file__)[0])
    user_agents_file = os.path.join(install_folder, 'user_agents.txt')
    with open(user_agents_file) as fp:
        user_agents_list = [_.strip() for _ in fp.readlines()]
except Exception:
    user_agents_list = [USER_AGENT]

def get_random_user_agent():
    """
    Get a random user agent string.

    :rtype: str
    :return: Random user agent string.
    """
    return random.choice(user_agents_list)