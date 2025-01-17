# gudlift-registration

## 1. Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

## 2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 

    This Fork of the project use Poetry as virtual Environnement.

## 3. Poetry as Virtual Environnement

Installation of Poetry:

   ```shell
    curl -sSL https://install.python-poetry.org | python3 - 
   ```

Enable the virtual Environment :

   ```shell
    poetry shell
   ```

Install Dependencies ( pyproject.toml or poetry.lock files must exist in the project -- they are the "requirements.txt"
equivalent for Poetry):

   ```shell
    poetry install 
   ```

Disable the Virtual Environment :

   ```shell
    exit
   ```

## 4. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

## 5. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

## 6. Testing

    The tests are done with Pytest.

Use the command to run the tests :

   ```shell
    pytest
   ```

or, to remove the warnings:

   ```shell
    pytest --disable-warnings
   ```

To have a more complete view, Coverage can be use too. Run The command :

   ```shell
   coverage run -m pytest
   ```

or, to remove the warnings:

   ```shell
    coverage run -m pytest --disable-warnings
   ```

which will looks similar to the command "pytest" but will allow to use ...

   ```shell
    coverage html
   ```

... to have more detail on the coverage of the code through
the html page generate (use the link given in response of the command).

