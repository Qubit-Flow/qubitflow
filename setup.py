from setuptools import setup, find_packages

setup(
    name='qubitflow',
    version='0.1.0',
    description='A modular and scalable quantum computing framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='G Sreejith',
    author_email='g.sreejith@outllok.com',
    url='https://github.com/qubit-flow/qubitflow',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

