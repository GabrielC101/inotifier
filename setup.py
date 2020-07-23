from setuptools import setup

setup(
    name='inotifier',
    version='0.1',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Programming Language :: Python :: 3'
    ],
    packages=['tests', 'inotifier'],
    url='https://github.com/GabrielC101/inotifier',
    license='Apache2',
    author='Gabriel Curio',
    install_requires=['inotify'],
    extras_requirements={
        'examples':
        [
            'inotifier.examples',
            'inotifier.examples.printer.printer',
            'inotifier.examples.renamer.renamer'
        ]
    },
    extras_require={
        "examples": ["psutil"],
    },
    description='Inotify Event Handler'
)
