import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gatetools",
    version="0.1",
    author="OpenGate collaboration",
    author_email="david.sarrut@creatis.insa-lyon.fr",
    description="Tools for GATE ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenGATE/GateTools",
    packages=['gatetools'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'uproot',
        'click',
        'pydicom',
        'tqdm',
        'colored',
        'itk',
        'unittest2',
      ],
    scripts=[
        'bin/gate_info',
        'bin/gate_image_uncertainty',
        'bin/gate_image_arithm',
        'bin/gate_image_convert',
        'bin/gate_gamma_index',
        ]
)
