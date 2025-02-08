{
  python3,
  stdenv,
  gtk3,
  gtk-layer-shell,
  cairo,
  gobject-introspection,
  libdbusmenu-gtk3,
  gdk-pixbuf,
  gnome-bluetooth,
  cinnamon-desktop,
  extraPythonPackages ? [],
  extraBuildInputs ? [],
}: let
  python = python3.withPackages (
    ps:
      with ps;
        [
          click
          pycairo
          pygobject3
          loguru
          psutil
          python-fabric
          pygobject-stubs
        ]
        ++ extraPythonPackages
  );
in
  stdenv.mkDerivation {
    name = "run-widget";
    propagatedBuildInputs =
      [
        gtk3
        gtk-layer-shell
        cairo
        gobject-introspection
        libdbusmenu-gtk3
        gdk-pixbuf
        gnome-bluetooth
        cinnamon-desktop
      ]
      ++ extraBuildInputs;
    phases = ["installPhase"];
    installPhase = ''
      mkdir -p $out/bin
      cat > $out/bin/run-widget << EOF
      #!/bin/sh
      GI_TYPELIB_PATH=$GI_TYPELIB_PATH \
      ${python.interpreter} "\$@"
      EOF
      chmod +x $out/bin/run-widget
    '';
    meta.mainProgram = "run-widget";
  }
