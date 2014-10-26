#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-common
Name:		lxqt-common
Version:	0.8.0
Release:	0.3
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b48d6df01f23d56115448076ae875680
Patch0:		startlxqt.patch
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	xz-devel
Requires:	liblxqt >= 0.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-common.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake \
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/sessions

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a $RPM_BUILD_ROOT/usr/share/xsessions/*.desktop $RPM_BUILD_ROOT%{_sysconfdir}/X11/sessions/
rm -rf $RPM_BUILD_ROOT/usr/share/xsessions
rm -rf $RPM_BUILD_ROOT/usr/share/apps/kdm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/startlxqt
%dir %{_datadir}/lxqt
%{_datadir}/lxqt/graphics
%dir %{_sysconfdir}/qt5/lxqt
%{_sysconfdir}/qt5/lxqt/*.conf
%{_datadir}/lxqt-qt5/openbox
%dir %{_sysconfdir}/qt5/pcmanfm-qt
%dir %{_sysconfdir}/qt5/pcmanfm-qt/lxqt
%{_sysconfdir}/qt5/pcmanfm-qt/lxqt/*.conf
%{_sysconfdir}/xdg/autostart/lxqt*.desktop
%{_sysconfdir}/X11/sessions/lxqt.desktop
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/ambiance
%{_datadir}/lxqt/themes/a-mego
%{_datadir}/lxqt/themes/light
%{_datadir}/lxqt/themes/flat
%{_datadir}/lxqt/themes/green
%{_datadir}/lxqt/themes/flat-dark-alpha
%{_datadir}/lxqt/themes/plasma-next-alpha

