Name: 		minitube
Version: 	1.4.2
Release: 	%mkrel 1
Summary:        A native YouTube client
Group:          Video
License:        GPLv2+
URL:            http://flavio.tordini.org/minitube
Source:         http://flavio.tordini.org/files/minitube/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel
BuildRequires:  phonon-devel

%description
Minitube is a native YouTube client. With it you can watch YouTube videos in
a new way: you type a keyword, Minitube gives you an endless video stream.
Minitube does not require the Flash Player.

Minitube is not about cloning the original Youtube web interface, it strives
to create a new TV-like experience.

%prep
%setup -q -n minitube

%build
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc TODO CHANGES AUTHORS
%{_bindir}/minitube
%{_datadir}/applications/minitube.desktop
%{_datadir}/icons/hicolor/*/apps/minitube.*
%{_datadir}/minitube

