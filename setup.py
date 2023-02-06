import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='livestream_saver',  # this should be unique
    include_package_data=True,
    version='0.0.0',
    author='Test User',
    author_email='udemy@test.com',
    description='This is preprocessing package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Aproved :: MIT License',
        "Operating System :: OS Independent"],
    python_requires='>=3.5'
)
