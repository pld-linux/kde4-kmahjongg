%define		_state		stable
%define		orgname		kmahjongg
%define		qtver		4.8.0

Summary:	KDE Mahjongg clone
Summary(pl.UTF-8):	Klon gry Mahjongg dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo Mahjongg para o KDE
Name:		kde4-%{orgname}
Version:	4.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c71bc4742a6afd4bc6d0ef2f821f2a2b
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	kde4-libkmahjongg-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a clone of the well known Mahjongg game.

%description -l pl.UTF-8
Wersja KDE znanej gry Mahjongg.

%description -l pt_BR.UTF-8
Versão do jogo Mahjongg para o KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_desktopdir}/kde4/kmahjongg.desktop
%{_datadir}/apps/kmahjongg
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_iconsdir}/*/*/apps/kmahjongg.png
%{_iconsdir}/*/*/apps/kmahjongg.svgz
