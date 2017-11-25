from conans import ConanFile, CMake

class Base64Conan(ConanFile):
    name = "base64"
    version = "1.0.2"
    url = "https://github.com/DEGoodmanWilson/base64.git"
    license = "BSD"
    settings = "os", "compiler", "build_type", "arch"
    options = {"build_base64_tests":    [True, False]}
    default_options = "build_base64_tests=False"
    generators = "cmake"
    exports = ["*"]

    def config(self):
        if self.options.build_base64_tests:
            self.requires.add("gtest/1.7.0@lasote/stable", private=False)
            self.options["gtest"].shared = False
        else:
            if "gtest" in self.requires:
                del self.requires["gtest"]

    def build(self):
        cmake = CMake(self)
        build_base64_tests = "-DBUILD_BASE64_TESTS=ON" if self.options.build_base64_tests else "-DBUILD_BASE64_TESTS=OFF"

        self.run('cmake %s %s %s' % (build_base64_tests, self.conanfile_directory, cmake.command_line))
        self.run('cmake --build . %s' % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="./")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["base64"]
