cmake_minimum_required (VERSION 3.12)

project("DSCSRenderer")
set(CMAKE_SHARED_LIBRARY_PREFIX="")

add_library(${PROJECT_NAME} STATIC
            "libs/glad/src/glad.c"
            "src/DSCS/Renderer.cpp"
            "src/DSCS/DataObjects/AnimationSampler.cpp" 
            "src/DSCS/DataObjects/OpenGLDSCSMaterial.cpp"
            "src/DSCS/DataObjects/OpenGLDSCSMesh.cpp"
            "src/DSCS/DataObjects/OpenGLDSCSTexture.cpp" 
            "src/DSCS/DataObjects/SkeletonDataBlocks.cpp"
            "src/DSCS/RenderObjects/Camera.cpp"
            "src/DSCS/ShaderSystem/cgGL/cgGLShaderBackend.cpp"
            "src/DSCS/ShaderSystem/cgGL/cgGLShaderObject.cpp"
            "src/DSCS/ShaderSystem/cgGL/Utils.cpp" 
            "src/DSCS/ShaderSystem/cgGL/OpenGLSettings/OpenGLSettings.cpp"  
            "src/FileFormats/DSCS/DSCStoOpenGL.cpp" 
            "src/FileFormats/DSCS/AnimFile/AnimReadWrite.cpp" 
            "src/FileFormats/DSCS/GeomFile/GeomReadWrite.cpp"
            "src/FileFormats/DSCS/GeomFile/MaterialReadWrite.cpp"
            "src/FileFormats/DSCS/GeomFile/MeshReadWrite.cpp" 
            "src/FileFormats/DSCS/NameFile/NameReadWrite.cpp"
            "src/FileFormats/DSCS/SkelFile/SkelReadWrite.cpp" 
            "src/FileFormats/Textures/DDS.cpp"  
            "src/serialisation/Exceptions.cpp"
            "src/serialisation/ReadWriter.cpp" 
            "src/Utils/BitManip.cpp"
            "src/Utils/Float16.cpp"
            "src/Utils/Hashing.cpp"
            "src/Utils/Matrix.cpp"
            "src/Utils/OpenGL.cpp"
            "src/Utils/Vector.cpp"
 )

# Set up Cg
# Static
if (WIN32)
    target_link_libraries(${PROJECT_NAME} 
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/cg.lib"
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/cgGL.lib"
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/glut32.lib")

    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/cg.dll"  ${${PROJECT_NAME}_BINARY_DIR}/cg.dll
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/cgGL.dll" ${${PROJECT_NAME}_BINARY_DIR}/cgGL.dll
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/windows/glut32.dll" ${${PROJECT_NAME}_BINARY_DIR}/glut32.dll
    )
endif (WIN32)
if (APPLE)
    target_link_libraries(${PROJECT_NAME} 
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/mac/libCg.dylib")

    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/mac/libCg.dylib" ${${PROJECT_NAME}_BINARY_DIR}/libCg.dylib
    )
endif(APPLE)
if (UNIX AND NOT APPLE)
    target_link_libraries(${PROJECT_NAME} 
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/linux64/libCg.so"
        "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/linux64/libCgGL.so")

    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/linux64/libCg.so" ${${PROJECT_NAME}_BINARY_DIR}/libCg.so
        COMMAND ${CMAKE_COMMAND} -E copy "${${PROJECT_NAME}_SOURCE_DIR}/libs/Cg/linux64/libCgGL.so" ${${PROJECT_NAME}_BINARY_DIR}/libCgGL.so
    )
endif(UNIX AND NOT APPLE)
