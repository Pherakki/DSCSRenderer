# DSCSRenderer
A C++ library for loading and rendering DSCS models into an OpenGL context. Currently in a usable, albeit unpleasant repository state. The project currently has a lot of bad code and compiler warnings that should be fixed with subsequent work. See build instructions below.

## API
[to be written]

## Building
### C++ with CMake
The library does provide a pure C API so you should build the library as part of your program to ensure ABI compatibility. The CMakeLists.txt is set up to build a static library. To include this in your CMake project:

1) Include the repository as a subdirectory of your repository.
2) Add the following lines to your CMakeLists.txt:

`add_subdirectory(path/to/DSCSRenderer)`

`target_link_libraries(${PROJECT_NAME} DSCSRenderer)`

Your CMakeLists.txt should then build the library and link it against your program. Remember to distribute the required Cg shared libraries included in the DSCSRenderer repository with your program. These should be packaged in an easy-to-copy format by this repository's CMakeLists.txt in the future.

### Python with Cython
1) Run `python setup.py build_ext --inplace` in the repository directory
2) The files required for distribution will be copied into a `dist` folder.

### More?
Hopefully more build options (and more stable) build options will appear in the future. Examples of projects that currently build and use the library:

https://github.com/TakafumiSakagami/DSCS_CC

https://github.com/Pherakki/DSCSModelDataEditor
