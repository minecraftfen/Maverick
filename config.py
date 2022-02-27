# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "/blog/qinqiang/"
build_dir = "./dict/"
template = "Galileo"
index_page_size = 3
archives_page_size = 10
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": True,
    "repo": "minecraftfen/minecraftfen.github.io@gh-pages"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "秦腔"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2022-01-16T12:00+08:00"
author = "Ivor"
email = "Ivorling041@gmail.com"
author_homepage = "https://minecraftfen.github.io"
description = "这里是秦腔发展的研究所,研究秦腔与其他文化融合的尝试"
key_words = ["Maverick", "Qinqiang", "秦腔", "blog", "博客"]
language = 'zh-cn'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "博客系统提供者"
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/minecraftfen/",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "IKRAfuPq0zrz6Wfje8ahHAIP-gzGzoHsz",
    "appKey": "lFaCWkd4xCs0Ng5UWs1eHNwU",
    "visitor": True,
    "recordIP": True
}

head_addon = ''

footer_addon = ''

body_addon = ''

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "buinPe10YWQL78kEE8eCknOP-gzGzoHsz",
    "appKey": "jsGLFxQFfiIyhpxypbp01qKe",
    'avatar': 'hide'
}
