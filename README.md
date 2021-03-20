# MATFILES

a library to read in all versions of mat files into
python. 

## Current Status: 
I am just beginning to implement v7.3 loading. Once I
get that working I am planning on using scipy to load
older versions of mat files and just wrapping its
functionality

## TODO:
- [ ] Implement loading v7.3 mat files into a dictionary

    - [ ] Add functionality to ascertain a version of file and fall back to scipy for v7.2 and lower

    - [ ] Add functionality to reset the global namespace instead of returning a dictionary

- [ ] Implement saving the global namespace into a mat file to load again or into Matlab. 
    
    - [ ] v7.3
    
    - [ ] v7.2 and lower