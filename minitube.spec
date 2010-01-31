%define name    minitube
%define version 0.9
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        A native YouTube client.
Group:          Video
License:        GPLv2
URL:            http://flavio.tordini.org/minitube
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  libqt4-devel
BuildRequires:  phonon-devel

%description
Minitube is a native YouTube client. With it you can watch YouTube videos in a new
way: you type a keyword, Minitube gives you an endless video stream. Minitube does
not require the Flash Player.

Minitube is not about cloning the original Youtube web interface, it strives to
create a new TV-like experience.

%prep
%setup -q -n minitube

%build
qmake PREFIX=%{buildroot}%{_prefix}
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/minitube
%{_datadir}/applications/minitube.desktop
%{_datadir}/minitube/locale/*.qm
%{_datadir}/icons/hicolor/*/apps/minitube.png
%{_datadir}/icons/hicolor/scalable/apps/minitube.svg
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/minitube
%dir %{_datadir}/minitube/locale

