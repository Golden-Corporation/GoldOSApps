import os # lets you use command line features
import json # used for reading metadata

metadatafile = open(r"/var/cache/Gversion.txt", "r")
MetaData = json.loads(metadatafile.read()) 
# past two lines used for metadata, you can ignore but don't delete it.

os.system(f'sudo mkdir /usr/gosapps/{MetaData['Name']}') # makes your program file. used for pretty much everything you need to store,
# path is /usr/gosapps/{your metadata name}

os.system('sudo apt-get examplePlsRemove -f') # example command
# put sudo installs here like "os.system('sudo apt-get foo -f') and remember to add the -f flag please!
# note that you can put as many installs as you like here but please don't make it take too long!

# you can copy your files here, remember you can use the $PWD variable to use local paths.
os.system('sudo cp $PWD/app.py /usr/gosapps/ExampleApp') # example command
