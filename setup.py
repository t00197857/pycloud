__author__ = 'jdroot'

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

pip_session = PipSession()

#Parse the requirements file
reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', session=pip_session)]

setup(
    name='pycloud',
    version='0.1',
    description='Cloudlet Server',
    author='Software Engineering Institute',
    author_email='James Root <jdroot@sei.cmu.edu>',
    url='',
    install_requires=reqs,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={
        'templates': ['pycloud/manager/templates/*'],
        'public': ['pycloud/manager/public/**.*'],
        'xml': ['*.xml']
    },
    entry_points="""
    [console_scripts]
    pycloud=pycloud:main

    [paste.app_factory]
    api = pycloud.api:make_app
    manager = pycloud.manager:make_app

    [paste.app_install]
    api = pylons.util:PylonsInstaller
    manager = pylons.util:PylonsInstaller
    """
)