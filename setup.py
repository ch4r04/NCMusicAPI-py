from setuptools import setup, find_packages


setup(
    name='NCMusicAPI-py',

    version='1.1.0',

    description='NetEase Cloud Music Api',
    long_description="NeteaseCloudMusicAPI-python",

    url='https://github.com/ch4r04/NCMusicAPI-py.git',

    author='ch4r0n',
    author_email='xingrenchan@gmail.com',

    license='MIT',

    classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',

            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],

    keywords='netEase music api python',

    # You can just specify the packages manually here if your project is
    packages=["NCMusicAPI"],
        # simple. Or you can use find_packages().
    install_requires=['requests', 'pony'],

    # List additional groups of dependencies here
        extras_require={},
    )
