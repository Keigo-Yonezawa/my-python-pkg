import os

from setuptools import find_packages, setup


PACKAGE_DIRNAME = 'my_python_pkg'
ROOT_DIR = os.path.dirname(__file__)

with open(os.path.join(ROOT_DIR, 'README.md')) as readme:
    README = readme.read()


def get_version() -> str:
    """packageのバージョンを取得します
    実体は `PACKAGE_DIRNAME / version.py` に記載しておいてそれを取得するしくみ
    """
    version_filepath = os.path.join(ROOT_DIR, PACKAGE_DIRNAME, 'version.py')
    with open(version_filepath) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split()[-1][1:-1]
    assert False

def _lines_from_file(filename):
    with open(os.path.join(ROOT_DIR, filename)) as f:
        lines = f.readlines()
    return lines

def get_extra_requires():
    extras = {
        # テスト用のパッケージ
        'test': ['pytest'],
        # ドキュメント生成用パッケージ
        'document': ['sphinx', 'sphinx_rtd_theme']
    }
    return extras


setup(
    name='my-python-pkg',
    version=get_version(),
    author='yone_kaggle',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='',
    long_description=README,
    long_description_content_type='text/markdown',
    author_email='keigo20000306@gmail.com',
    install_requires=_lines_from_file('requirements.txt'),
    extras_require=get_extra_requires(),
    classifiers=[
        # ライセンス情報とか
        'Framework :: Matplotlib',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)