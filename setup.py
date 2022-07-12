from distutils import sysconfig
import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import shutil
from sys import platform

from Cython.Build import cythonize

# Link the correct libraries
cg_include_dirs=["libs/Cg"]
if platform == "linux" or platform == "linux2":
    cg_library_dir = "libs/Cg/linux64"
    cg_libraries=['libCg', 'libCgGL']
    cgsobj_suffix = "so"
    pysobj_suffix = "so"
elif platform == "darwin":
    cg_library_dir = "libs/Cg/mac"
    cg_libraries=['libCg']
    cgsobj_suffix = "dylib"
    pysobj_suffix = "dylib"
elif platform == "win32":
    cg_library_dir = "libs/Cg/windows"
    cg_libraries=['cg', 'cgGL', 'glut32']
    cgsobj_suffix = "dll"
    pysobj_suffix = "pyd"
else:
    raise Exception("Unsupported platform: ", platform)


# Generate dict of compiler args for different compiler versions
BUILD_ARGS = {}
for compiler, args in [
        ('msvc', ['/std:c++20']),
        ('gcc', ['-std=c++2a']),
        ('g++', ['-std=c++2a']),
        ('clang', ['-std=c++20']),
        ('clang++', ['-std=c++20']),
        ('unix', ['-std=c++2a'])]:
    BUILD_ARGS[compiler] = args
    
# https://stackoverflow.com/a/40193040
def get_ext_filename_without_platform_suffix(filename):
    name, ext = os.path.splitext(filename)
    ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')

    if ext_suffix == ext:
        return filename

    ext_suffix = ext_suffix.replace(ext, '')
    idx = name.find(ext_suffix)

    if idx == -1:
        return filename
    else:
        return name[:idx] + ext

class CustomBuildExt(build_ext):
    def build_extensions(self):
        compiler = self.compiler.compiler_type
        args = BUILD_ARGS[compiler]
        for ext in self.extensions:
            ext.extra_compile_args = args
        build_ext.build_extensions(self)

    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        return get_ext_filename_without_platform_suffix(filename)

# Now compile
package_name = "pyDSCSRenderer"
setup(
    name=package_name,
    cmdclass={ 'build_ext': CustomBuildExt },
    ext_modules = [Extension(
       package_name,
       sources=[
           "pyDSCSRenderer.pyx",
           "libs/glad/src/glad.c",
           "src/DSCS/Renderer.cpp",
           "src/DSCS/DataObjects/AnimationSampler.cpp",
           "src/DSCS/DataObjects/OpenGLDSCSMaterial.cpp",
           "src/DSCS/DataObjects/OpenGLDSCSMesh.cpp",
           "src/DSCS/DataObjects/OpenGLDSCSTexture.cpp",
           "src/DSCS/DataObjects/SkeletonDataBlocks.cpp",
           "src/DSCS/RenderObjects/Camera.cpp",
           "src/DSCS/ShaderSystem/cgGL/cgGLShaderBackend.cpp",
           "src/DSCS/ShaderSystem/cgGL/cgGLShaderObject.cpp",
           "src/DSCS/ShaderSystem/cgGL/Utils.cpp",
           "src/DSCS/ShaderSystem/cgGL/OpenGLSettings/OpenGLSettings.cpp",
           "src/FileFormats/DSCS/DSCStoOpenGL.cpp",
           "src/FileFormats/DSCS/AnimFile/AnimReadWrite.cpp",
           "src/FileFormats/DSCS/GeomFile/GeomReadWrite.cpp",
           "src/FileFormats/DSCS/GeomFile/MaterialReadWrite.cpp",
           "src/FileFormats/DSCS/GeomFile/MeshReadWrite.cpp",
           "src/FileFormats/DSCS/NameFile/NameReadWrite.cpp",
           "src/FileFormats/DSCS/SkelFile/SkelReadWrite.cpp",
           "src/FileFormats/Textures/DDS.cpp",
           "src/serialisation/Exceptions.cpp",
           "src/serialisation/ReadWriter.cpp",
           "src/Utils/BitManip.cpp",
           "src/Utils/Float16.cpp",
           "src/Utils/Hashing.cpp",
           "src/Utils/Matrix.cpp",
           "src/Utils/OpenGL.cpp",
           "src/Utils/Vector.cpp"
       ],
       language="c++",
       include_dirs=[*cg_include_dirs],
       library_dirs =[cg_library_dir],
       libraries=[*cg_libraries]
   )]
)

os.makedirs("dist", exist_ok=True)
compiled_sobj = os.extsep.join((package_name, pysobj_suffix))
dest_path = os.path.join("dist", compiled_sobj)
if os.path.exists(dest_path):
    os.remove(dest_path)
shutil.copy2(compiled_sobj, dest_path)
for item in cg_libraries:
    item = os.extsep.join((item, cgsobj_suffix))
    dest_path = os.path.join("dist", item)
    if os.path.exists(dest_path):
        continue
    shutil.copy2(os.path.join(cg_library_dir, item), dest_path)
