#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-common
Name:		lxqt-common
Version:	0.10.0
Release:	0.9
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	6bf2c06e0de15da33a054bb02b681b02
Patch0:		startlxqt.patch
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	xz-devel
Requires:	liblxqt >= 0.10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-common.

%prep
%setup -q
#%patch0 -p0

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xsessions/lxqt.desktop
%{_sysconfdir}/qt5/autostart/lxqt-compton.desktop
%{_sysconfdir}/qt5/autostart/lxqt-desktop.desktop
%{_sysconfdir}/qt5/autostart/lxqt-globalkeyshortcuts.desktop
%{_sysconfdir}/qt5/autostart/lxqt-notifications.desktop
%{_sysconfdir}/qt5/autostart/lxqt-panel.desktop
%{_sysconfdir}/qt5/autostart/lxqt-policykit-agent.desktop
%{_sysconfdir}/qt5/autostart/lxqt-powermanagement.desktop
%{_sysconfdir}/qt5/autostart/lxqt-qlipper-autostart.desktop
%{_sysconfdir}/qt5/autostart/lxqt-runner.desktop
%{_sysconfdir}/qt5/autostart/lxqt-xscreensaver-autostart.desktop
%{_sysconfdir}/qt5/lxqt/lxqt.conf
%{_sysconfdir}/qt5/lxqt/session.conf
%{_sysconfdir}/qt5/lxqt/windowmanagers.conf
%{_sysconfdir}/qt5/menus/lxqt-applications.menu
%{_sysconfdir}/qt5/pcmanfm-qt/lxqt/settings.conf
%attr(755,root,root) %{_bindir}/startlxqt
%{_datadir}/desktop-directories/lxqt-leave.directory
%{_datadir}/desktop-directories/lxqt-settings.directory
%{_iconsdir}/hicolor/scalable/places/start-here-lxqt.svg
%{_datadir}/kdm/sessions/lxqt.desktop
%dir %{_datadir}/lxqt/graphics
%{_datadir}/lxqt/graphics/README
%{_datadir}/lxqt/graphics/helix.svg
%{_datadir}/lxqt/graphics/helix_1120.png
%{_datadir}/lxqt/graphics/helix_150.png
%{_datadir}/lxqt/graphics/helix_60.png
%{_datadir}/lxqt/graphics/helix_lxqt.svg
%{_datadir}/lxqt/graphics/lxqt_logo.png
%{_datadir}/lxqt/graphics/lxqt_logo_doxygen.png
%{_datadir}/lxqt/graphics/spacer-dark-dots.svg
%{_datadir}/lxqt/graphics/spacer-dark-line.svg
%{_datadir}/lxqt/graphics/spacer-light-dots.svg
%{_datadir}/lxqt/graphics/spacer-light-line.svg
%dir %{_datadir}/lxqt/openbox
%{_datadir}/lxqt/openbox/menu.xml
%{_datadir}/lxqt/openbox/rc.xml.in
%dir %{_datadir}/lxqt/themes
%dir %{_datadir}/lxqt/themes/ambiance
%{_datadir}/lxqt/themes/ambiance/Butterfly-Kenneth-Wimer.jpg
%{_datadir}/lxqt/themes/ambiance/arrow-left.svg
%{_datadir}/lxqt/themes/ambiance/arrow-right.svg
%{_datadir}/lxqt/themes/ambiance/lxqt-notificationd.qss
%dir %{_datadir}/lxqt/themes/ambiance/lxqt-notificationd
%{_datadir}/lxqt/themes/ambiance/lxqt-notificationd/cancel.svg
%{_datadir}/lxqt/themes/ambiance/lxqt-panel.qss
%{_datadir}/lxqt/themes/ambiance/lxqt-runner.qss
%dir %{_datadir}/lxqt/themes/ambiance/lxqt-runner
%{_datadir}/lxqt/themes/ambiance/lxqt-runner/clear.svg
%{_datadir}/lxqt/themes/ambiance/lxqt-runner/navigation-menu.svg
%{_datadir}/lxqt/themes/ambiance/mainmenu.svg
%{_datadir}/lxqt/themes/ambiance/preview.png
%dir %{_datadir}/lxqt/themes/ambiance/spacer-plugin
%{_datadir}/lxqt/themes/ambiance/spacer-plugin/spacer-dots.svg
%{_datadir}/lxqt/themes/ambiance/spacer-plugin/spacer-line.svg
%{_datadir}/lxqt/themes/ambiance/wallpaper.cfg
%dir %{_datadir}/lxqt/themes/dark
%{_datadir}/lxqt/themes/dark/arrow-right.svg
%dir %{_datadir}/lxqt/themes/dark/calendar-popup
%{_datadir}/lxqt/themes/dark/calendar-popup/left-arrow.svg
%{_datadir}/lxqt/themes/dark/calendar-popup/right-arrow.svg
%{_datadir}/lxqt/themes/dark/lxqt-notificationd.qss
%dir %{_datadir}/lxqt/themes/dark/lxqt-notificationd
%{_datadir}/lxqt/themes/dark/lxqt-notificationd/cancel.svg
%{_datadir}/lxqt/themes/dark/lxqt-panel.qss
%{_datadir}/lxqt/themes/dark/lxqt-runner.qss
%dir %{_datadir}/lxqt/themes/dark/lxqt-runner
%{_datadir}/lxqt/themes/dark/lxqt-runner/close.svg
%{_datadir}/lxqt/themes/dark/lxqt-runner/down-arrow.svg
%{_datadir}/lxqt/themes/dark/mainmenu.svg
%{_datadir}/lxqt/themes/dark/preview.png
%dir %{_datadir}/lxqt/themes/dark/spacer-plugin
%{_datadir}/lxqt/themes/dark/spacer-plugin/spacer-dots.svg
%{_datadir}/lxqt/themes/dark/spacer-plugin/spacer-line.svg
%{_datadir}/lxqt/themes/dark/wallpaper.cfg
%{_datadir}/lxqt/themes/dark/wallpaper.png
%dir %{_datadir}/lxqt/themes/frost
%{_datadir}/lxqt/themes/frost/arrow-right.svg
%dir %{_datadir}/lxqt/themes/frost/calendar-popup
%{_datadir}/lxqt/themes/frost/calendar-popup/left-arrow.svg
%{_datadir}/lxqt/themes/frost/calendar-popup/right-arrow.svg
%{_datadir}/lxqt/themes/frost/debug.png
%{_datadir}/lxqt/themes/frost/lxqt-notificationd.qss
%{_datadir}/lxqt/themes/frost/lxqt-panel.qss
%{_datadir}/lxqt/themes/frost/lxqt-runner.qss
%dir %{_datadir}/lxqt/themes/frost/lxqt-runner
%{_datadir}/lxqt/themes/frost/lxqt-runner/close.svg
%{_datadir}/lxqt/themes/frost/lxqt-runner/down-arrow.svg
%{_datadir}/lxqt/themes/frost/mainmenu.svg
%{_datadir}/lxqt/themes/frost/numix.png
%{_datadir}/lxqt/themes/frost/preview.png
%dir %{_datadir}/lxqt/themes/frost/spacer-plugin
%{_datadir}/lxqt/themes/frost/spacer-plugin/spacer-dots.svg
%{_datadir}/lxqt/themes/frost/spacer-plugin/spacer-line.svg
%dir %{_datadir}/lxqt/themes/frost/volume-plugin
%{_datadir}/lxqt/themes/frost/volume-plugin/mixer.svg
%{_datadir}/lxqt/themes/frost/wallpaper.cfg
%dir %{_datadir}/lxqt/themes/kde-plasma
%{_datadir}/lxqt/themes/kde-plasma/kde-plasma.png
%{_datadir}/lxqt/themes/kde-plasma/left-arrow.svg
%{_datadir}/lxqt/themes/kde-plasma/lxqt-notificationd.qss
%dir %{_datadir}/lxqt/themes/kde-plasma/lxqt-notificationd
%{_datadir}/lxqt/themes/kde-plasma/lxqt-notificationd/window-close.svg
%{_datadir}/lxqt/themes/kde-plasma/lxqt-panel.qss
%{_datadir}/lxqt/themes/kde-plasma/lxqt-runner.qss
%dir %{_datadir}/lxqt/themes/kde-plasma/lxqt-runner
%{_datadir}/lxqt/themes/kde-plasma/lxqt-runner/application-menu.svg
%{_datadir}/lxqt/themes/kde-plasma/lxqt-runner/close-32x32.png
%{_datadir}/lxqt/themes/kde-plasma/lxqt-runner/close-48x48.png
%{_datadir}/lxqt/themes/kde-plasma/lxqt-runner/window-close.svg
%{_datadir}/lxqt/themes/kde-plasma/mainmenu.svg
%{_datadir}/lxqt/themes/kde-plasma/preview.png
%{_datadir}/lxqt/themes/kde-plasma/right-arrow.svg
%dir %{_datadir}/lxqt/themes/kde-plasma/spacer-plugin
%{_datadir}/lxqt/themes/kde-plasma/spacer-plugin/spacer-dots.svg
%{_datadir}/lxqt/themes/kde-plasma/spacer-plugin/spacer-line.svg
%{_datadir}/lxqt/themes/kde-plasma/wallpaper.cfg
%dir %{_datadir}/lxqt/themes/light
%{_datadir}/lxqt/themes/light/96640-simple_blue_widescreen.svg
%dir %{_datadir}/lxqt/themes/light/lxqt-lightdm-greeter
%{_datadir}/lxqt/themes/light/lxqt-lightdm-greeter/dropdown.svg
%{_datadir}/lxqt/themes/light/lxqt-lightdm-greeter/leaveIcon.svg
%{_datadir}/lxqt/themes/light/lxqt-notificationd.qss
%{_datadir}/lxqt/themes/light/lxqt-panel.qss
%dir %{_datadir}/lxqt/themes/light/lxqt-panel
%{_datadir}/lxqt/themes/light/lxqt-panel/plugin-handle-horizontal.gif
%{_datadir}/lxqt/themes/light/lxqt-panel/plugin-handle-vertical.gif
%{_datadir}/lxqt/themes/light/lxqt-runner.qss
%dir %{_datadir}/lxqt/themes/light/lxqt-runner
%{_datadir}/lxqt/themes/light/lxqt-runner/close-32x32.png
%{_datadir}/lxqt/themes/light/lxqt-runner/close-48x48.png
%{_datadir}/lxqt/themes/light/mainmenu.svg
%{_datadir}/lxqt/themes/light/preview.png
%{_datadir}/lxqt/themes/light/simple_blue_widescreen.png
%dir %{_datadir}/lxqt/themes/light/spacer-plugin
%{_datadir}/lxqt/themes/light/spacer-plugin/spacer-dots.svg
%{_datadir}/lxqt/themes/light/spacer-plugin/spacer-line.svg
%{_datadir}/lxqt/themes/light/wallpaper.cfg
