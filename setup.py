import setuptools
import zipfile
import glob

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "dummy-package",
    "version": "0.0.1",
    "author": "Douglas A. C. Martins",
    "author_email": "douglasacmartins@yahoo.com",
    "description": "POC for pytest and package builder",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/douglasacmartins/dummy-package",
    "project_urls": {
        "Bug Tracker": "https://github.com/douglasacmartins/dummy-package",
    },
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    "package_dir": {"": "src"},
    "packages": setuptools.find_packages(where='src'),
    "python_requires": ">3.6,<3.8"
}

setuptools.setup(**setup_info)

if __name__ == "__main__":
    """
        Mount an simple AWS Lambda Layer
    """
    packages_paths = [
        '/'.join(package.split('.'))
        for package in setup_info["packages"]
    ]
    zip_name = f'dist/{setup_info["name"]}-{setup_info["version"]}.zip'
    package_dirs = list(setup_info['package_dir'].items())

    with zipfile.ZipFile(zip_name, 'w') as zf:
        for zip_dir, source in package_dirs:
            for paths in packages_paths:
                for each in glob.glob(
                    f'{source}/{paths}/*.py',
                    recursive=False
                ):
                    zf_path = each.replace(f"{zip_dir or source}/", "")
                    zf_path = f'python/{zf_path}'
                    zf.write(each, arcname=zf_path)
