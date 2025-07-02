{
  description = "The next-generation framework for building desktop widgets using Python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs =
    {
      self,
      nixpkgs,
      ...
    }:
    let
      inherit (nixpkgs) lib;
      systems = lib.genAttrs [
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = f: systems (system: f nixpkgs.legacyPackages.${system});
    in
    {
      formatter = forAllSystems (pkgs: pkgs.nixfmt-rfc-style);

      packages = forAllSystems (pkgs: rec {
        default = pkgs.callPackage ./default.nix { };
        python-fabric = default;
        run-widget =
          lib.warn
            "`run-widget` is deprecated and is going to be removed in future releases of fabric. refer to the wiki for more information."
            pkgs.callPackage
            ./run-widget.nix
            { inherit python-fabric; };
      });

      devShells = forAllSystems (
        pkgs:
        let
          inherit (self.packages.${pkgs.system}) python-fabric;
        in
        {
          default = pkgs.mkShell {
            name = "fabric-shell";
            inputsFrom = [ python-fabric ];
            packages = [
              python-fabric
              pkgs.ruff
            ];
          };
        }
      );

      overlays.default = final: prev: { inherit (self.packages.${prev.system}) python-fabric; };
    };
}
