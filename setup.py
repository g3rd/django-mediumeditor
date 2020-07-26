from setuptools import setup

long_description = open('README.md').read()

setup(
    name="dj-mediumeditor",
    version='1.0.0',
    packages=["dj_mediumeditor"],
    include_package_data=True,
    description="Medium Editor widget for Django",
    url="https://github.com/abedyngash/dj-mediumeditor",
    author="Abedy Ng'ang'a",
    author_email="abedy.nganga@gmail.com",
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
    install_requires=[
        'django-appconf >= 1.0.2',
    ],
)
