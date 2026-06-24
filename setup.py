from setuptools import setup
setup(
    name="325-router", version="1.0.0",
    description="Smart AI model router by Empire325Marketing. Classify prompts, route to optimal model tier.",
    long_description=open("README.md").read(), long_description_content_type="text/markdown",
    author="Empire325Marketing", url="https://empire325marketing.com",
    packages=["325_router"], package_dir={"325_router": "src/325_router"},
    entry_points={"console_scripts": ["325=325_router:cli"]},
    python_requires=">=3.8",
    classifiers=["License :: OSI Approved :: MIT License","Programming Language :: Python :: 3"],
)
