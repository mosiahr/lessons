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
   <title>{}</title>
</head>

<body>
   <header></header>
   <main></main>
   <footer></footer>
</body>

</html>'''

def create_html_file(path='index.html', title=None):
    if ispath(path):
        print(f"A '{path}' file already exists! The file isn't created!")
    else:
        with open(path, 'w') as f:
            f.write(DEFAULT_INDEX_HTML.format(title or DEFAULT_TITLE_NAME))
            print(f"A '{path}' file is created successfully!")

def create_gitignore(path='.gitignore'):
    if ispath(path):
        print(f"A '{path}' file already exists! The file isn't created!")
    else:
        with open(path, 'w') as f:
            print(f"A '{path}' file is created successfully!")

def ispath(path):
    if os.path.exists(path):
        return True
    return False

def create_folder(path):
    if ispath(path):
        print(f"A '{path}' folder already exists! The folder isn't created!")
    else:
        os.makedirs(path)
        print(f"A '{path}' folder is created successfully!")


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

        file_path = os.path.join(path, '.gitignore')
        create_gitignore(file_path)

    # Note: Create HTML file require project directory is created.
    if is_args:
        create_html_file(os.path.join(project_dir, 'index.html'), title=project_dir)
    else:
        create_html_file(os.path.join(project_dir, 'index.html'))