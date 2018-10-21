from setuptools import setup, find_packages

files = ["NCMusicAPI/*"]
setup(
    name='NCMusicAPI',
    version='1.3.1',
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

    keywords='Netease Music API',
    # You can just specify the packages manually here if your project is
    py_modules=["NCMusicAPI"],
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    include_package_data=True,
    install_requires=['requests',
                      'pony >= 0.7.6'],
    zip_safe=False
    # List additional groups of dependencies here
    )
