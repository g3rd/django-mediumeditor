from setuptools import setup

long_description = open('README.md').read()

setup(
    name="django-mediumeditor",
    version='0.1.1',
    packages=["mediumeditor"],
    include_package_data=True,
    description="Medium Editor widget for Django",
    url="https://github.com/g3rd/django-mediumeditor",
    author="Chad Shryock",
    author_email="chad@aceportfol.io",
    license='MIT',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
