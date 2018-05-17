# Downloader

Specifically Created to download dataset to download activitynet dataset
Link:http://ec2-52-11-11-89.us-west-2.compute.amazonaws.com/files/activity_net.v1-3.min.json

I installed youtube-dl in linux to a virtual environment named 'tensorflow'
So in execute.sh I activate & deactivate tensorflow environment. Change the virtual environment name to your setting (or remove if you installed it wothout a environment)
There should be a 'DataSet' directory with the files (execute.sh and arrange.py and dataset.json)

In both execute.sh and arrange.py the variable 'path' should be edited to the directory path where all of these execution files exists
Videos will be download into the DataSet directory

No execeptions will be handled. You are on your own. I'm too lazy to make it friendly

run the following command in linux shell (current directory should be where those execution files are)

sh execute.sh

If the process is long on your sense, Or you have to close the terminal just use below

nohup execute.sh &

and you can close terminal and it will be download in background
