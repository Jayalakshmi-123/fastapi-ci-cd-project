from setuptools import setup, find_packages

setup(
    name="fastapi_ci_cd_demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "psycopg2-binary",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "fastapi-demo=app.main:app",
        ],
    },
)
