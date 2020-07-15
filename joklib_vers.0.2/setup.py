import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='joklib',  
     version='0.2',
     author="Jan-Ole G. (J-O. technik)",
     author_email="j-o.technik@web.de",
     description="A library for J-O. Techniks Klimaboxen",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/jotechnik/joklib_library",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )