import conans

class CoroConanTestPackage(conans.ConanFile):
    settings   = "os", "build_type", "arch", "compiler"
    generators = "cmake_find_package"

    def build(self):
        cmake = conans.CMake(self)

        cmake.definitions["CMAKE_CXX_FLAGS_INIT"] = f"-stdlib=libc++"

        cmake.configure()

        cmake.build()
    
    def test(self):
        self.run("./CoroConanTestPackage")
