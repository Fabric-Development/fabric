{
  description = ''
    next-gen framework for building desktop widgets using Python
    (check the rewrite branch for progress)
  '';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem (
      system: let
        overlay = final: prev: {
          pythonPackagesExtensions =
            prev.pythonPackagesExtensions
            ++ [
              (python-final: python-prev: {
                python-fabric = prev.callPackage ./default.nix {};
              })
            ];
        };

        pkgs = nixpkgs.legacyPackages.${system}.extend overlay;
      in {
        overlays.default = overlay;
        formatter = pkgs.nixfmt-rfc-style;
        packages = {
          default = pkgs.python3Packages.python-fabric;
          run-widget = pkgs.callPackage ./run-widget.nix {};
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
              gnome-bluetooth
              cinnamon-desktop
              (python3.withPackages (
                ps:
                  with ps; [
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
