#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class Base64Conan(ConanFile):
    name = "base64"
    version = "1.0.2"
    generators = "cmake"
    author = "DEGoodmanWilson"
    url = "https://github.com/{0}/conan-{1}".format(author, name)
    description = "Base64 encode and decode routines by René Nyffenegger"
    license = "https://github.com/{0}/conan-{1}/blob/master/LICENSES".format(author, name)
    exports_sources = ["CMakeLists.txt", "LICENSE",\
                       "base64.cpp", "base64.h",\
                       "tests/CMakeLists.txt", "tests/basic_functioning.cpp", "tests/main.cpp",\
                       "test_package/CMakeLists.txt", "test_package/conanfile.py", "test_package/test_package.cpp"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    # build_requires = "gtest/1.8.0@bincrafters/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
       # self.run('ctest . --verbose')

    def package(self):
        self.copy(pattern="LICENSE")
        self.copy(pattern="*.h", dst="include/{0}".format(self.name))
        self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
