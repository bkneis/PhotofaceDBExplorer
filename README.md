## Photoface DB Explorer

This repo is meant to act as a tool to be used with the photo face database.

It contains a python notebook to show the data structure and visualize the districution of subjects in the database.

It also has a useful python script, create_csv.py. This script is used to transform the subject images and create a csv file that can be imported by the opencv examples within the face recognition module. This should allow you to run all opencv face examples on the database. For more information on the opencv examples, please visit http://docs.opencv.org/3.0-beta/modules/face/doc/facerec/facerec_tutorial.html#face-recognition

#### How do I run it locally?
The repo uses anaconda to create a virtual environment so that there is no conflict with python version or dependencies.
First install conda if you have not already got it
Visit https://conda.io/docs/user-guide/install/index.html for more info on how to do so

Clone this repo
``git clone https://github.com/bkneis/PhotofaceDBExplorer && cd PhotofaceDBExplorer``

Now create the anaconda environment
``conda env create -f environment.yml``

Activate the environment
``source .env``

To create the csv file for opencv examples, run:
``python create_csv.py /path/to/photofacedb``

To run the notebook locally:
``jupyter notebook``
