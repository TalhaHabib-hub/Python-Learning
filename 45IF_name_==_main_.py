'''
if_name_==_main_.py in python
The if if_name_==_main_.py idiom is a common  pattern used in python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the _name_ variable is a built-in variable that is automatically set to the name of the current module. when a python script is run directly, the _name_variable is set to the string _main_ when the script is imported as a module into script, the _name_ variable is set to the name of the module.

Here's an example of how the if _name_ == main idiom can be used

def main():
    # code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__"
    main()

In this example, the main function contains the code that should be run when the script is run directly. The if statment at the bottom checks whether the _name_ variable is equal to _main_. if it is, the main function is called.

'''
import Talha    # Talha is a file
Talha.welcome()
''' on something like a shell harry bhai  wrote this.     
# python Talha.py 
this executed the function inside the Talha.py file
then
# python main.py
this executed the function twice although it makes sense of one time the the function got executed because we had imported and also called it in the main file but why for the second time?
The reason is when we are importing the Talha file the function in it are also executing inside in the main file But we have to avoid it the function calls need to be only there where the are in the file if the file is imported we don't want everything in that file got executed we just want that only those things should be executed which only we want
for that we will go to the file which we are imporring (lets go to Talha.py)
'''