from setuptools import setup

setup(
    name = "Tenlo Stock Watcher",
    version = "0.0"
    description = "Use historical data to analyze stock",
    url = "https://github.com/GitMazzone/tenlo-stock-watcher",
    author = "Michael Mazzone",
    author_email = "contact@michael-mazzone.com",
    license = "MIT",
    packages = ["stocksave"],
    install_requires = [
        "scrapy",
        "pystock-crawler",
        "schedule"
    ],
    zip_safe = False
    )
