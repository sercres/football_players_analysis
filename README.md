In order to run the code, some steps must be done first:


## Using a virtual environment
It is heavily recommended to use a virtual environment to run the code.

## Installing the requirements

The following code needs some modules to run. In order to do so, you must install the requirements on the requirements.txt file.
Two instructions are shown just to showcase how to install the requirements file outside of the project folder, or in the project folder,
you just have to install one according to your circumstances:

- Make sure that you are using your virtual environment
- If you are outside the project folder, run the following command: pip install -r /path/to/requirements.txt
- Or if you are in the project folder, run the following command: pip install -r requirements.txt


- Wait until the installation is done. You now got all the modules required to run the code.

## Executing the code

There are several .py files with the code corresponding to each exercise. For instance, for exercise1 there is ex1.py.
On those py files with the code of the exercises there is only the code corresponding the the functions.
In order to run the analysis that are required in exercises, such as 2c, there is a main.py file that runs those analysis.

- So, in order to have the output of the analysis requested, you must run: python3 main.py

- In order to run the public tests, you must run: python3 -m tests.test_public
- In ordre to run the custom tests, you must run: python3 -m tests.test_custom

In order to check the code styling, it is recommended to run each py file separately.

- To check ex1 styling, run: pylint ex1.py
- The same instruction but changing the .py file will give the individual result of the code styling.
- In order to run all the styling on all the files, run: pylint *.py
