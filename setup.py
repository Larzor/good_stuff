import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='good_to_have',
    version='0.0.1',
    author='Anders Larsson',
    author_email='laseranders@gmail.com',
    description='good stuff',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Larzor/good_stuff',
    project_urls = {
        "Bug Tracker": "https://github.com/Larzor/good_stuff/issues"
    },
    license='MIT',
    packages=['good_to_have'],
    install_requires=['requests']
)