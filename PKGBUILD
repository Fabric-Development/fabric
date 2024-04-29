# Maintainer: Yousef El-Darsh <yousef.eldarsh@gmail.com>

pkgname=python-fabric-git
reponame=fabric
pkgver=0.0.1
pkgrel=1
pkgdesc="next-gen GTK+ based desktop widgets python framework"
arch=(any)
url="http://github.com/Fabric-Development/fabric"
license=('unknown')
groups=()
depends=(
    gtk3
    cairo
    gtk-layer-shell
    libgirepository
    gobject-introspection
    gobject-introspection-runtime
    python
    python-pip
    python-gobject
    python-cairo
    python-loguru
    python-click
    pkgconf
)
makedepends=(
    python-setuptools
    meson-python
    ninja
    meson
    git
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

source=(git+http://github.com/Fabric-Development/$reponame.git)

sha256sums=("SKIP")

prepare() {
  cd "$srcdir/$reponame"
  git submodule update --init
}

build() {
  cd "$srcdir/$reponame"
  meson --prefix=/usr build
  ninja -C build
}

package() {
  cd "$srcdir/$reponame"
  DESTDIR="$pkgdir" meson install -C build
}
