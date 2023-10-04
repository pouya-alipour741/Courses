####install venv via command console
# python -m venv venv

###Deactivate environment
# deactivate

####list everything in that directory
#dir

###cd to change path to a directory or use cd ../ to go back a folder   or cd foldername to go forward


###clear screen
#cls

######activate environment
# first change to venv directory then type scripts\activate.bat


#########show packages installed
#pip list
#pip freeze


#########install requirement file
# pip freeze then copy it into a requirement.txt file then pip install -r requirements.txt

####rmdir venv /s to remove that directory and sub dirs even if not empty

###mkdir venv to creat folder venv


### creat venv that have all the global packages ,new packages installed in this venv wont affect global
# python -m venv venv --system-site-packages

###only shows packages that are installed in this venv and do not exist in global
#pip list --local


#####update
# $ pip install --upgrade <package-name>
# $ pip install -U <package-name>

#########for jupyter
"""first python -m venv venv    as usual then change to that directory using cd then
pip install ipykernel
then python -m ipykernel install --user --name=venv_name

then ipython kernel install --name "venv-name" --user   ##this line must be wrong
note: you can change venv via jupyter kernel tab anytime"""

##spectate kernels in jupytor
# jupyter kernelspec list

###uninstall
##jupyter kernelspec uninstall myenv

