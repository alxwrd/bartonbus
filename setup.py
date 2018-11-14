from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='bartonbus',
    packages=['bartonbus'],
    version='0.0',
    description='A Python wrapper around Trent Barton''s live bus times',
    author='Alex Ward',
    author_email='alxwrd@googlemail.com',
    url='https://github.com/alxwrd/bartonbus',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['requests', 'maya'],
    license='MIT',
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/alxwrd/bartonbus',
        'Bug Reports':  'https://github.com/alxwrd/bartonbus/issues',
    }
)
