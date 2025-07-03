{
  lib,
  pkg-config,
  wrapGAppsHook3,
  gobject-introspection,
  python3,
  python3Packages,
  runtimeShell,
  gtk3,
  gtk-layer-shell,
  cairo,
  libdbusmenu-gtk3,
  gdk-pixbuf,
  cinnamon-desktop,
  gnome-bluetooth,
  extraPackages ? [ ],
  extraDependencies ? [ ],
}:
let
  pydeps =
    ps:
    with ps;
    [
      click
      pycairo
      pygobject3
      pygobject-stubs
      loguru
      psutil
    ]
    ++ extraDependencies;
in
python3Packages.buildPythonPackage {
  pname = "python-fabric";
  version = "0.0.2";
  pyproject = true;

  src = ./.;

  build-system = [ python3Packages.setuptools ];

  nativeBuildInputs = [
    pkg-config
    gobject-introspection
    wrapGAppsHook3
  ];

  buildInputs = [
    gtk3
    gtk-layer-shell
    cairo
    gobject-introspection
    libdbusmenu-gtk3
    gdk-pixbuf
    cinnamon-desktop
    gnome-bluetooth
  ] ++ extraPackages;

  dependencies = pydeps python3Packages;

  postInstall =
    let
      py = python3.withPackages pydeps;
    in
    ''
      mkdir -p $out/bin
      cat > $out/bin/fabric << EOF
      #!${runtimeShell}
      export PYTHONPATH="${toString ./.}:${py}/lib/python${py.python.version}/site-packages"
      GI_TYPELIB_PATH=$GI_TYPELIB_PATH \
      GDK_PIXBUF_MODULE_FILE="$GDK_PIXBUF_MODULE_FILE" \
      ${py.interpreter} -m fabric "\$@"
      EOF
      chmod +x $out/bin/fabric
    '';

  meta = {
    changelog = "https://github.com/Fabric-Development/fabric/blob/master/CHANGELOG.md";
    description = "The next-generation framework for building desktop widgets using Python";
    homepage = "https://github.com/Fabric-Development/fabric";
    license = lib.licenses.agpl3Plus;
    maintainers = with lib.maintainers; [ ];
  };
}
