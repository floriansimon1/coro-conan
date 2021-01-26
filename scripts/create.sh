#!/bin/bash

scriptDirectory="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

rm -rf ~/.conan/data/coro

conan create "${scriptDirectory}/.." coro/20201021@florian/game --profile="${scriptDirectory}/../conan-profile"
