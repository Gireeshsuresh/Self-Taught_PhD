#  conda list : lists the packages in all the environments 
# -n followed by the name of the anaconda env whose package list you want to export to the text file. (ex) -n myenv . // Here 'myenv' is the name of the env and is specified by the '-n' flag.
#  The 'blah.txt' is the name of the text file which consists of the list of packages that was exported from the given environment.

conda list -n cv --explicit > ./cv_env_packageList_python_3.8.5.txt
