from setuptools import setup, find_packages

setup(name='funniest',
      version='0.1',
      description='Encryptor',
      long_description='Bytes to encrypt string and encrypted string to bytes.',
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