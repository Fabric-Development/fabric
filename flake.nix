{
  description = ''
    next-gen framework for building desktop widgets using Python
    (check the rewrite branch for progress)
  '';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/24.05";
    utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, utils, ... }:
    utils.lib.eachDefaultSystem (
      system:
      let
        overlay = final: prev: {
          pythonPackagesExtensions = prev.pythonPackagesExtensions ++ [
            (python-final: python-prev: {
              python-fabric = prev.callPackage ./default.nix { };
            })
          ];
        };

        pkgs = nixpkgs.legacyPackages.${system}.extend overlay;
      in
      {
        overlays.default = overlay;
        formatter = pkgs.nixfmt-rfc-style;
        packages = {
          default = pkgs.python3Packages.python-fabric ;
          run-widget =
            let
              python = pkgs.python3.withPackages (
                ps: with ps; [
                  click
                  pycairo
                  pygobject3
                  loguru
                  psutil
                  python-fabric
                  pygobject-stubs
                ]
              );
            in
            pkgs.stdenv.mkDerivation {
              name = "run-widget";
              propagatedBuildInputs = with pkgs; [
                gtk3
                gtk-layer-shell
                cairo
                gobject-introspection
                libdbusmenu-gtk3
                gdk-pixbuf
                gnome.gnome-bluetooth
                cinnamon.cinnamon-desktop
              ];
              phases = [ "installPhase" ];
              installPhase = ''
                mkdir -p $out/bin
                cat > $out/bin/run-widget << EOF
                #!/bin/sh
                GI_TYPELIB_PATH=$GI_TYPELIB_PATH \
                ${python.interpreter} "\$@"
                EOF
                chmod +x $out/bin/run-widget
              '';
            };
        };

        devShells = {
          default = pkgs.mkShell {
            name = "fabric-shell";
            packages = with pkgs; [
              ruff
              gtk3
              gtk-layer-shell
              cairo
              gobject-introspection
              libdbusmenu-gtk3
              gdk-pixbuf
              gnome.gnome-bluetooth
              cinnamon.cinnamon-desktop
              (python3.withPackages (
                ps: with ps; [
                  setuptools
                  wheel
                  build
                  click
                  pycairo
                  pygobject3
                  pygobject-stubs
                  loguru
                  psutil
                  python-fabric
                ]
              ))
            ];
          };
        };
      }
    );
}
