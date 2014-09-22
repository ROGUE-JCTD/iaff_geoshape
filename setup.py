from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils not to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
geonode_dir = 'iaff_rogue'

for dirpath, dirnames, filenames in os.walk(geonode_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


setup(name='iaff_geoshape',
      version='0.0.1',
      description="Application for serving and sharing geospatial data",
      long_description=open('README.md').read(),
      classifiers=[
        "Development Status :: 4 - Beta"],
      keywords='',
      author='Noblis NSP',
      author_email='rogue@lmnsolutions.com',
      url='http://rogue.lmnsolutions.com',
      license='GPL',
      packages=packages,
      data_files=data_files,
      install_requires=[
        "requests==2.4.1"
        ],
      zip_safe=False,
      )