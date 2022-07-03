# DSCSRenderer
A C++ library for loading and rendering DSCS models into an OpenGL context.

## API
[to be written]

## Building
### C++ with CMake
1) Include the repository as a subdirectory of your respository.
2) Add the following lines to your CMakeLists.txt:

`add_subdirectory(path/to/DSCSRenderer)`

`target_link_libraries(${PROJECT_NAME} DSCSRenderer)`

Your CMakeLists.txt should then build the library and link it against your program. Remember to distribute the required Cg shared libraries included in the DSCSRenderer repository with your program. These should be packaged in an easy-to-copy format by this repository's CMakeLists.txt in the future.

### Python
1) Run `python setup.py build_ext --inplace` in the repository directory
2) The files required for distribution will be copied into a `dist` folder.
