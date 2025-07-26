%global commit0 c203ffe80f4e7b68e22ba3fde0598622500f5add
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:           hyprpanel
Version:        1.git%{shortcommit0}
Release:        1
Summary:        A panel built for Hyprland with Astal
License:        MIT
URL:            https://github.com/Jas-SinghFSU/HyprPanel
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  sass
BuildRequires:  aylur-gtk-shell
BuildRequires:  meson
BuildRequires:  gjs

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
