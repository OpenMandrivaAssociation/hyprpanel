# Untested
%global commit0 0a961ce8a959c521f41546af7f355e04adee5503
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2
%global debug_package %{nil}

Name:           hyprpanel
Version:        1.0.0.%{bumpver}~.git%{shortcommit0}
Release:        1
Summary:        A panel built for Hyprland with Astal
License:        MIT
URL:            https://github.com/Jas-SinghFSU/HyprPanel
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:	%{name}-pnpm-offline-cache.tar.gz
BuildRequires:  sass
BuildRequires:  aylur-gtk-shell
BuildRequires:  meson
BuildRequires:  gjs
BuildRequires:	pnpm

Requires:       bluez
Requires:       sass
Requires:       lib64wireplumber
Requires:       wl-clipboard
Requires:       aylur-gtk-shell
Requires:       bluez
Requires:       gnome-bluetooth
Requires:       gvfs
Requires:       typelib(NM)
Requires:       typelib(GTop)
Requires:       NetworkManager
Requires:       upower
Requires:       fonts-ttf-nerd-jetbrains-mono
Requires:       python-gpustat
Requires:       wf-recorder
Requires:       matugen
Requires:       grimblast
Requires:       gjs
Requires:       lib64soup-gir3.0

Recommends:     ppd-service
Suggests:       tuned-ppd

Recommends:     brightnessctl
Recommends:     btop
Recommends:     grimblast
Recommends:     hypridle
Recommends:     hyprpicker
Recommends:     hyprsunset
Recommends:     jq
Recommends:     swww
Recommends:     wf-recorder

Provides:       HyprPanel

%description
%{summary}.

%prep
%autosetup -n HyprPanel-%{commit0} -p1
tar zxf %{S:1}
rm -rf node_modules/astal
ls
mkdir -p node_modules/astal
cp -ra %{_datadir}/astal/gjs/* node_modules/astal

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}/usr/share/fonts
mv %{buildroot}%{_datadir}/%{name}/assets/fonts %{buildroot}%{_datadir}/fonts/nf-hyprpanel


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/fonts/nf-hyprpanel
