Name:		minitube
Version:	2.4
Release:	1
Summary:	A native YouTube client
Group:		Video
License:	GPLv2+
URL:		http://flavio.tordini.org/minitube
Source0:	https://github.com/flaviotordini/minitube/archive/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	phonon-devel
Requires:	phonon-backend
Requires:	gstreamer0.10-ffmpeg
Suggests:	gstreamer0.10-faad

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
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%doc TODO CHANGES AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}
