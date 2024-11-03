#!/usr/bin/env python

import os
import sys

DEFAULT_DIR_NAME = 'new_project'
DIR_LIST = ['css', 'fonts', 'img', 'js']
DEFAULT_TITLE_NAME = 'Document'

DEFAULT_INDEX_HTML = '''<!DOCTYPE html>
<html lang="en">

<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="css/style.css">
   <title>{}</title>
</head>

<body>
   <div class="wrapper">
      <header class="header">
         <div class="header__container">
         </div>
      </header>
      <main class="page">
         <div class="page__container">
            <div class="page__">

			</div>
			<div class="page__">

			</div>
			<div class="page__">

			</div>
		 </div>
      </main>
      <footer class="footer">
         <div class="footer__container">
            <span>© 2024 Gregory</span>
         </div>
      </footer>
   </div>
</body>

</html>'''

DEFAULT_STYLE_CSS = \
'''/* Local fonts */
@import url('fonts.css');

/* Reset */
@import url('reset.css');

.wrapper {
    min-height: 100%;
    overflow: hidden;
}
'''

DEFAULT_RESET_CSS = \
'''*,
*::before,
*::after {
	padding: 0;
	margin: 0;
	border: none;

	box-sizing: border-box;
}
*::before,
*::after {
	display: inline-block;
}

a {
	text-decoration: none;
	display: inline-block;
	color: inherit;
}
li {
	list-style: none;
}
img {
	vertical-align: top;
}
html,
body {
	line-height: 1;
	height: 100%;
}
h1,
h2,
h3,
h4,
h5,
h6 {
	font-weight: inherit;
	font-size: inherit;
}

/* FORM */
input,
button,
textarea {
	font-family: inherit;
	font-size: inherit;
	line-height: inherit;
	color: inherit;
	background-color: transparent;
}
input,
textarea {
	width: 100%;
}
button,
select,
option {
	cursor: pointer;
}
input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
	appearance: none;
}
'''

def ispath(path):
    if os.path.exists(path):
        return True
    return False

def create_file(path, text=''):
    if ispath(path):
        print(f"The '{path}' file already exists! The file isn't created!")
    else:
        with open(path, 'w') as f:
            f.write(text)
            print(f"The '{path}' file is created successfully!")

def create_folder(path):
    if ispath(path):
        print(f"The '{path}' folder already exists! The folder isn't created!")
    else:
        os.makedirs(path)
        print(f"The '{path}' folder is created successfully!")


if __name__ == '__main__':
    try:
        project_dir = sys.argv[1]
        is_args = True
    except IndexError:
        project_dir = DEFAULT_DIR_NAME
        is_args = False

    for item in DIR_LIST:
        path = os.path.join(project_dir, item)
        create_folder(path)
        create_file(os.path.join(path, '.gitignore'))

    # Note: Create HTML file require project directory is created.
    if is_args:
        create_file(os.path.join(project_dir, 'index.html'), 
                    DEFAULT_INDEX_HTML.format(project_dir.capitalize()))
    else:
        create_file(os.path.join(project_dir, 'index.html'), 
                    DEFAULT_INDEX_HTML.format(DEFAULT_TITLE_NAME))

    create_file(os.path.join(project_dir, 'css/style.css'), DEFAULT_STYLE_CSS)
    create_file(os.path.join(project_dir, 'css/reset.css'), DEFAULT_RESET_CSS)
    create_file(os.path.join(project_dir, 'css/fonts.css'))


