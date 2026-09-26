# I made a folder in a document then and this one is incomplete

# Virtual Environment
'''A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

to create a virtual environment in python, we can use the venv module that comes with python. Here's an example of how th create virtual environment and activate it:

# Create a virtual evironment
python -m venv myenv

# Activate the virtual environment(Linus/macOS)
source myenv/bin/activate

# Activate the virtual environment (windows)
myenv\Scripts\activate.bat,  ps1 for power shell

Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global python environment. This allows you to have a seperate set of packages for each project, wihtout affecting the packages installed in the global environment'''


#the "requirememts.txt" file
# In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that Talha your project depends on. This file can be used easily install all the required packages in a new environment.
# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and version. for example

'''
# Output the list of installed packages and their versions to file 
---> pip freeze > requirements.txt
 to install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:
#Install th packages listed in the requirements.txt file
---> pip install -r requirements.txt


Using virtual environment and a requirements.txt file can help you manage the dependecies for Talha your python projects and ensure that Talha your projectsare portable and can easily be set up on a new machine
'''

'''
Everting used



'''