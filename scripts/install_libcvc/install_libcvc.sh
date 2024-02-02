# !/usr/bin/env bash

cinnamon_git="https://github.com/linuxmint/cinnamon-desktop"
cinnamon_git_name="cinnamon-desktop"
cwd="$(pwd)"

pre_check_exists() {
    # check if Cvc typelibs are installed
    echo "checking if libcvc is already installed..."
    if ls /usr/lib/girepository-1.0/Cvc-1.0.typelib 1> /dev/null 2>&1;
    then
        echo "typelib files are already installed, reinstall? [y/n] (default: n)";
        read answer
        if [ "$answer" != "${answer#[Yy]}" ]; then
            echo "do you want to remove existing files? [y/n] (default: n)"
            read answer2
            if [ "$answer2" != "${answer2#[Yy]}" ]; then
                sudo rm -rf /usr/lib/girepository-1.0/Cvc-1.0.typelib
                sudo rm -rf /usr/share/gir-1.0/Cvc-1.0.gir
                sudo rm -rf /usr/lib/libcvc.s*
            fi
        else
            exit 0
        fi
    else
        echo "typelib files not found, check meson logs";
    fi
}

prepare() {
    pre_check_exists
    mkdir -p ignore_me_libcvc_build
    cd ignore_me_libcvc_build
    git clone ${cinnamon_git}
    patch -i ../$(dirname $0)/meson.build.patch ${cwd}/ignore_me_libcvc_build/${cinnamon_git_name}/meson.build
    # ^ we shorten the build time by removing unused build targets
}

build() {
    # patch and build
    cd ${cwd}/ignore_me_libcvc_build/${cinnamon_git_name}
    meson build
    cd build
    ninja
}

check_gir() {
    # check if gir files got generated
    cd ${cwd}/ignore_me_libcvc_build/${cinnamon_git_name}/build
    if ls libcvc/*.gir 1> /dev/null 2>&1;
        then echo "gir files got generated, proceeding to install";
    else
        echo "gir files not found, check meson logs";
        exit 1
    fi
}

install_gir() {
    # install gir files
    cd ${cwd}/ignore_me_libcvc_build/${cinnamon_git_name}/build
    meson install
    cd libcvc
    sudo cp -r libcvc.s* /usr/lib/
    sudo cp Cvc-1.0.typelib /usr/lib/girepository-1.0/
    sudo cp Cvc-1.0.gir /usr/share/gir-1.0/
}

clean_exit() {
    rm -rf ${cwd}/ignore_me_libcvc_build
    exit 0
}

prepare
build
check_gir
install_gir
clean_exit
