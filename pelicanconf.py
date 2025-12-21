#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kartik'
SITENAME = "Kartik Mathur"
SITEURL = 'https://kmathur.github.io/kartikblog'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),)

# Social widget
SOCIAL = (('GitHub', '#'),
          ('Twitter', '#'),
          ('LinkedIn', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme settings
THEME = 'themes/flex'

# Flex theme specific settings
SITETITLE = SITENAME
SITESUBTITLE = 'Notes, musings, and reflections<br>on stuff that captures my curiosity'
SITEDESCRIPTION = 'Midnight thoughts on technology, poetry, and life'
SITELOGO = 'https://kmathur.github.io/kartikblog/images/profile.JPG'

# Clean, minimal styling similar to reference site
MAIN_MENU = True
MENUITEMS = (
    ('About', 'https://kmathur.github.io/kartikblog/pages/about-me.html'),
    ('Thoughts', 'https://kmathur.github.io/kartikblog/pages/thoughts.html'),
    ('Archive', 'https://kmathur.github.io/kartikblog/archives.html'),
)

# Disable some features for cleaner look
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Social links in footer
SOCIAL = (
    ('github', 'https://github.com/kmathur'),
    ('twitter', 'https://x.com/kartik_mathur'),
    ('linkedin', 'https://www.linkedin.com/in/mathurkartik/'),
)

# Clean pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Flex theme additional settings for clean look
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3
DISPLAY_ARCHIVE_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISABLE_URL_HASH = True

# Clean header and footer
COPYRIGHT_YEAR = 2024
COPYRIGHT_NAME = AUTHOR

# Minimal home page
INDEX_SAVE_AS = 'index.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Custom CSS and static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

CUSTOM_CSS = 'static/custom.css'

# Favicon - use absolute path for all pages
FAVICON = '/favicon.ico'

# GitHub Pages settings
RELATIVE_URLS = False