from setuptools import setup

setup(name='file2db',
      version='1.2.8',
      description='Sync content between a table within a database and flat files',
      url='http://github.com/karmab/file2db',
      author='Karim Boumedhel',
      author_email='karimboumedhel@gmail.com',
      license='GPL',
      scripts=['file2db.py', 'samples/settings.py'],
      install_requires=[
          'antiorm',
          'click',
          'db',
          'db-sqlite3',
          'Flask',
          'itsdangerous',
          'Jinja2',
          'MarkupSafe',
          'psycopg2',
          'SQLAlchemy',
          'Werkzeug'

      ],
      zip_safe=False)
