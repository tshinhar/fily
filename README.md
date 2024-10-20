# Fily
a cli tool from file managment.

the tool currently supports orginzing all files in a given directory as well as removing all duplicate files under the given root directory
to use, simpley run the python code and pass it the root directory you want to perform the operation on, as well as the wanted option.
by default, removig duplicates will be used, for example:
`python main {path_to_dir}`
the tool will go over all files in the directory and any sub-directories under it and will list all the duplicate files before removing them.
by default, the script will ask before removing each of the files, if you want to allow the script to delete all duplicate files without asking, run:
`python main %cd% -y`

to orgenize files. you would need to select one of the available options:
`python main %cd% -o`
this option will orgenize all files to directories based on thier file extensions
`python main %cd% -o`
this option will orgenize all files to directories based on some common logic, for example, all images will be moved to an "images" 
directory, videos to "movies" directory, ect

if you want to be able to access the tool from any directory, you would need to add it to PATH
