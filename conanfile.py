import os
import conans

commit_by_version = {
    "20201021": "38ea89cda9cc17ddf43777c61b56dd4c695dcd22"
}

class CoroConanfile(conans.ConanFile):
    settings        = "os", "build_type", "arch", "compiler"
    url             = "https://github.com/Quuxplusone/coro.git"

    def source(self):
        if (
            self.settings.os != "Linux"
            or self.settings.arch != "x86_64"
            or self.settings.compiler != "clang"
            or self.settings.compiler.version != 11
            or self.settings.compiler.libcxx != "libc++"
        ):
            raise conans.errors.ConanInvalidConfiguration("This recipe is not tested in the configuration you requested")

        self.run(f"git clone {self.url} .")

        self.run(f"git checkout {commit_by_version[self.version]}")

    def build(self):
        pass

    def package(self):
        self.copy(pattern = "*.h")
