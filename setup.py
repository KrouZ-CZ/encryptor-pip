from setuptools import setup, find_packages

setup(name='encryptor',
      version='0.1',
      description='Encryptor',
      classifiers=[
        'Programming Language :: Python :: 3.10'
      ],
      keywords='encr encrypt encryptor',
      url='https://github.com/KvantPro',
      author='KrouZ_CZ',
      author_email='random1qwe@google.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'cryptography',
      ],
      include_package_data=False,
      zip_safe=False)
