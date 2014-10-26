from setuptools import setup

setup(
  name='digitalocean_to_sshconfig',
  version='0.0.1',
  description='automatically add your droplets into your ssh config.',
  url='https://github.com/emre/digitalocean_to_sshconfig',
  author='Emre Yilmaz',
  author_email='mail@emreyilmaz.me',
  license='MIT',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
  ],
  py_modules=['do2sshconfig'],
  install_requires= ["stormssh", "clint", "python-digitalocean"],
  entry_points={
      'console_scripts': [
            'digitalocean_to_sshconfig=do2sshconfig:main',
      ],
  },
)