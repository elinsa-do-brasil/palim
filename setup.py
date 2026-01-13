from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="palim",
    version="0.0.1",
    description="Customizações upgrade-safe do sistema de tickets Palim",
    author="Palim Ltda",
    author_email="suporte@palim.com.br",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
