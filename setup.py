from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in managed_tech/__init__.py
from managed_tech import __version__ as version

setup(
	name="managed_tech",
	version=version,
	description="Managed Technology System",
	author="Haynie Research & Development, LLC",
	author_email="info@haynieresearch.us",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
