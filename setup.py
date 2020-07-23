from setuptools import setup

setup(
    name='inotifier',
    version='0.1',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Programming Language :: Python :: 2'
    ],
    packages=['tests', 'inotifier'],
    url='https://github.com/GabrielC101/filer',
    license='Apache2',
    author='Gabriel Curio',
    install_requires=['inotify', 'psutil'],
    extras_requirements={
        'examples':
        [
            'inotifier.examples',
            'inotifier.examples.printer.printer',
            'inotifier.examples.renamer.renamer'
        ]
    },
    description='Inotify Event Handler'
)
