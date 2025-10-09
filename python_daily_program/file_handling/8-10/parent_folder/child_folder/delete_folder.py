import os 

#os.removedirs("parent_folder") #error if the folder is not empty

os.chdir("parent_folder") # Change the current working directory to the parent folder
#os.removedirs("child_folder") # Remove the child folder inside the parent folder
#os.rmdir("child_folder") # Remove the child folder inside the parent folder
#os.remove("child_folder/demo.txt") # Remove the demo.txt file inside the child folder
os.removedirs("child_folder") # Remove the child folder inside the parent folder after removing the file inside it