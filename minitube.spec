Name:		minitube
Version:	3.0
Release:	1
Summary:	A native YouTube client
Group:		Video
License:	GPLv3+
URL:		http://flavio.tordini.org/minitube
Source0:	https://github.com/flaviotordini/minitube/archive/%{name}-%{version}.tar.gz

#Source1:	https://github.com/flaviotordini/media/archive/master/media-git157456a.tar.gz
Source1:	http-master.tar.gz
#Source2:	https://github.com/flaviotordini/http/archive/master/http-gite790e31.tar.gz
Source2:	idle-master.tar.gz
#Source3:	https://github.com/flaviotordini/idle/archive/master/idle-git6aa092d.tar.gz
Source3:	media-master.tar.gz

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	qt5-qttools
BuildRequires:	qmake5
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(mpv)

Requires:	phonon4qt5-vlc
Requires: vlc-plugin-gnutls

%description
Minitube is a native YouTube client. With it you can watch YouTube videos in
a new way: you type a keyword, Minitube gives you an endless video stream.
Minitube does not require the Flash Player.

Minitube is not about cloning the original Youtube web interface, it strives
to create a new TV-like experience.

If you have problems with video playback, try to switch to vlc Phonon backend
in KDE4 settings.

If you use GStreamer Phonon backend, it's recommended to install package
gstreamer0.10-faad from PLF or Restricted (ex-PLF) repository.


%prep
%setup -q -n %{name}-%{version}

%build
%qmake_qt5 \
	PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc TODO CHANGES AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}
