project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_output_dirs_setup()

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# when including QuaZip sources directly into a project, QUAZIP_STATIC should
# be defined explicitly to avoid possible troubles with unnecessary importing/exporting.
if (WIN32)
    add_definitions(-DQUAZIP_STATIC)
endif()

find_package(Qt5Core REQUIRED)
find_package(zlib REQUIRED)
find_package(quazip REQUIRED)

set(CMAKE_MACOSX_RPATH ON)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
if(APPLE)
    set(CMAKE_INSTALL_RPATH "@loader_path;@executable_path")
else()
    set(CMAKE_INSTALL_RPATH "$ORIGIN")
endif()

include_directories(example ${Qt5Core_INCLUDE_DIRS} ${quazip_INCLUDE_DIRS} ${zlib_INCLUDE_DIRS})
add_executable(example example.cpp)
target_link_libraries(example Qt5::Core ${quazip_LIBRARIES} ${zlib_LIBRARIES})
