#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt-common
Name:		lxqt-common
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	f1a64db07d04f686b584cc8952479910
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	xz-devel
Requires:	liblxqt >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-common.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
%{_datadir}/lxqt/graphics
%dir %{_sysconfdir}/qt4/lxqt
%{_sysconfdir}/qt4/lxqt/*.conf
%{_datadir}/lxqt/openbox
%dir %{_sysconfdir}/qt4/pcmanfm-qt
%dir %{_sysconfdir}/qt4/pcmanfm-qt/lxqt
%{_sysconfdir}/qt4/pcmanfm-qt/lxqt/*.conf
%{_sysconfdir}/xdg/autostart/lxqt*.desktop
%{_sysconfdir}/X11/sessions/lxqt.desktop
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/ambiance
%{_datadir}/lxqt/themes/a-mego
%{_datadir}/lxqt/themes/light
%{_datadir}/lxqt/themes/flat
%{_datadir}/lxqt/themes/green
