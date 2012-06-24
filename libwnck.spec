Summary:	General Window Manager interfacing for gnome utilities
Summary(pl):	Interfejs General Window Manager dla narz�dzi gnome
Name:		libwnck
Version:	0.7
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+2-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
General Window Manager interfacing for gnome utilities. This library
is a part of the gnome 2 platform.

%description -l pl
Og�lny interfejs zarz�dcy okien dla narz�dzi GNOME. Ta biblioteka jest
cz�ci� platformy GNOME 2.

%package devel
Summary:	Header files and documentation for libwnck
Summary(pl):	Pliki nag��wkowe i dokumentacja dla libwnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header, docs and development libraries for libwnck.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libwnck.

%package static
Summary:	Static libwnck libraries
Summary(pl):	Statyczne biblioteki libwnck
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libwnck libraries.

%description static -l pl
Statyczna wersja bibliotek libwnck.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %name.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
