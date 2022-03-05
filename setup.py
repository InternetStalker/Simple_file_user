from setuptools import setup
from simple_file_user import __version__, read
import os

scriptFolder = os.path.dirname(__file__)
ReadmePath = os.path.join(scriptFolder, "README.html")

projectUrls = {
    "Homepage": "https://github.com/InternetStalker/Simple_file_user",
    "Русскоязычная документация": "https://zen.yandex.ru/media/id/60856790ae47bf185f78b82d/zdravstvuite-eto-ne-statia-a-dokumentaciia-k-moemu-paketu-v-pypi-608f77907ffcba2d9e3b78fc?&"
}

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]

setup(name = 'simple_file_user',
    version = __version__,
    description = 'Package for easy working with files.',
    packages = ['simple_file_user'],
    author_email = 'internetstalcker@yandex.ru',
    include_package_data = True,
    zip_safe = False,
    long_description = read(ReadmePath),
    long_description_content_type = 'text/markdown',
    project_urls = projectUrls,
    keywords = 'files file',
    classifiers = classifiers,
    license = 'MIT')
