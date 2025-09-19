from setuptools import setup, find_packages
from grob_dash_theme import __version__

setup(
    name="GROB Dash Theme",
    version=__version__,
    description="A custom theme for Dash applications by GROB.",
    author="Michael Nierlich,  Philipp Jäger, Tobias Scheuermann",
    author_email="Michael.Nierlich@grob.de, "
                 "Philipp.Jaeger@grob.de, "
                 "Tobias.Scheuermann@grob.de",
    packages=find_packages(),
)
