# Maintainer: Yousef El-Darsh <yousef.eldarsh@gmail.com>

pkgname=python-fabric-git
reponame=fabric
pkgver=0.0.1
pkgrel=1
pkgdesc="next-gen framework for building desktop widgets using python"
arch=(any)
url="https://github.com/Fabric-Development/fabric"
license=("AGPL-3.0-or-later")
groups=()
depends=(
    gtk3
    cairo
    gtk-layer-shell
    libgirepository
    gobject-introspection
    gobject-introspection-runtime
    webkit2gtk-4.1
    libdbusmenu-gtk3
    python
    python-pip
    python-gobject
    python-cairo
    python-loguru
    python-click
    pkgconf
)
makedepends=(
    git
    python-setuptools
)
optdepends=(
    "python-psutil: for system stats, this package is a dependency of the bar example file"
)
provides=(
    python-fabric
)
conflicts=(
    python-fabric
)

source=(git+https://github.com/Fabric-Development/$reponame.git)
sha256sums=("SKIP")

pkgver() {
    cd "$srcdir/$reponame"
    printf "%s.r%s.%s" "$pkgver" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
    cd "$srcdir/$reponame"
    python setup.py build
}

package() {
    cd "$srcdir/$reponame"
    python setup.py install --root="$pkgdir/" --optimize=1
}
