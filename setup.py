from typing import List
from setuptools import setup, find_packages


def read_requirements() -> List[str]:
    with open('requirements.txt') as req:
        content = req.read()
        return content.split('\n')


setup(
    name='declutter-snaps',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        desnap=desnap.cli:cli
    """,
)
