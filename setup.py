from setuptools import setup
import os


README = open(os.path.abspath('README.rst')).read()


setup(
    name='letsencrypt-remote',
    version='0.3.0',
    long_description="\n\n".join([README]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4"],
    install_requires=[
        'click',
        'pyOpenSSL',
        'requests'],
    entry_points={
        'console_scripts': ['letsencrypt-remote = letsencrypt_remote:main']},
    pyackages=['letsencrypt_remote'])
