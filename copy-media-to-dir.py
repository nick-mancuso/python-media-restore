from shutil import copyfile
import os
import subprocess
import re

# finds full path to file with filename 
def find(name):
    args = '. -name ' + name
    outbytes = subprocess.check_output(['find', '.', '-name', name])
    outstring = outbytes.decode("utf-8")
    return outstring.replace('\\n', '')




# read in and create list of existing files
filepath = 'file_list_recursive_image_files.out'
existing_files = []

cnt = 1

with open(filepath) as fp:
   line = fp.readline()
   while line:
       existing_files.append(line.replace('\n', ''))
       line = fp.readline()


#print(existing_files)

# read in and create list of missing files
filepath = 'missing_files_with_paths.out'
missing_files = []

cnt = 1

with open(filepath) as fp:
   line = fp.readline()
   while line:
       missing_files.append(line.replace('\n', ''))
       line = fp.readline()

#print(missing_files)

# for each existing file, create dictionary entry with path
dictionary = {}

for e in existing_files:
    for m in missing_files:
        if e in m:
            dictionary[e] = m

#print(dictionary)
#print(len(dictionary))

# copy images to correct path
for file in dictionary:
    #copyfile("media/")
    filename_w_path = find(file).replace('\n', '')
    path = dictionary.get(file).rsplit('/', 1)[0]
    #print(path)
    cmd = 'mkdir -p media/' + path + ' && cp \"' + filename_w_path + '\" media/' + dictionary.get(file).replace('\\n', '')
    #print(cmd)
    os.system(cmd)
