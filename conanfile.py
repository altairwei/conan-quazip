from conans import ConanFile, CMake, tools

class QuazipConan(ConanFile):
    name = "quazip"
    version = "0.7.6"
    license = "LGPL-2.1, zlib/png"
    url = "https://github.com/altairwei/conan-quazip"
    description = "A Qt/C++ wrapper for Gilles Vollant's ZIP/UNZIP C package (minizip). Provides access to ZIP archives from Qt programs using QIODevice API."
    settings = "os", "compiler", "build_type", "arch"
    requires = "zlib/1.2.11@conan/stable"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="quazip")
        git.clone("https://github.com/stachenov/quazip.git", self.version)
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("quazip/CMakeLists.txt", "project(QuaZip)",
                              '''project(QuaZip)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="quazip")
        cmake.build()

    def build_id(self):
        self.info_build.options.shared = "shared_and_static"

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src="quazip")
        self.copy(pattern="*.h", dst="include/quazip", src="quazip/quazip")
        # QuaZIP explicitly specified STATIC and SHARED in add_library(), so 
        # BUILD_SHARED_LIBS and BUILD_STATIC_LIBS do not works.
        if self.options.shared:
            self.copy(pattern="*.dll", dst="bin", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", keep_path=False)
            self.copy(pattern="*.dylib*", dst="lib", keep_path=False)
        else:
            self.copy(pattern="*quazip.lib", dst="lib", keep_path=False)
            self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["quazip5d"] if self.settings.build_type == "Debug" else ["quazip5"]

