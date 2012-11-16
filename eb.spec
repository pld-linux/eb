#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library for accessing CD-ROM books
Summary(pl.UTF-8):	Biblioteka dostępu do książek na płytach CD-ROM
Name:		eb
Version:	4.4.3
Release:	2
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
# Source0-md5:	17dd1fade7ba0b82ce6e60f19fcbc823
URL:		http://www.sra.co.jp/people/m-kasahr/eb/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EB Library supports to access CD-ROM books of EB, EBG, EBXA, EBXA-C,
S-EBXA and EPWING formats. CD-ROM books of those formats are popular
in Japan. Since CD-ROM books themseves are stands on the ISO 9660
format, you can mount the discs by the same way as other ISO 9660
discs.

%description -l pl.UTF-8
Biblioteka EB pozwala na dostęp do książek na płytach CD-ROM w
formatach EB, EBG, EBXA, EBXA-C, S-EBXA oraz EPWING. Książki w tych
formatach są popularne w Japonii. Ponieważ książki na płytach jako
takie są plikami zapisanymi w formacie ISO 9660, można montować
takie płyty w taki sam sposób, jak inne płyty ISO 9660.

%package utils
Summary:	Utilities provided by EB library
Summary(pl.UTF-8):	Narzędzia dostarczane przez bibliotekę EB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
Utilities provided by EB library.

%description utils -l pl.UTF-8
Narzędzia dostarczane przez bibliotekę EB.

%package devel
Summary:	Header files for EB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki EB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for EB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki EB.

%package static
Summary:	Static EB library
Summary(pl.UTF-8):	Statyczna biblioteka EB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EB library.

%description static -l pl.UTF-8
Statyczna biblioteka EB.

%package apidocs
Summary:	EB API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki EB
Group:		Documentation

%description apidocs
API and internal documentation for EB library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki EB.

%prep
%setup -q

%build
%configure \
	--enable-samples \
	--enable-pthread \
	--enable-ebnet \
	--enable-ipv6 \
	--with-pkgdocdir=%{_docdir}/%{name}-apidocs-%{version} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
%find_lang ebutils

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README
%attr(755,root,root) %{_libdir}/libeb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeb.so.16

%files utils -f ebutils.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ebappendix
%attr(755,root,root) %{_bindir}/ebfont
%attr(755,root,root) %{_bindir}/ebinfo
%attr(755,root,root) %{_bindir}/ebrefile
%attr(755,root,root) %{_bindir}/ebstopcode
%attr(755,root,root) %{_bindir}/ebunzip
%attr(755,root,root) %{_bindir}/ebzip
%attr(755,root,root) %{_bindir}/ebzipinfo

%files devel
%defattr(644,root,root,755)
%{_sysconfdir}/eb.conf
%attr(755,root,root) %{_libdir}/libeb.so
%{_libdir}/libeb.la
%{_includedir}/eb
%{_aclocaldir}/eb4.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libeb.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-apidocs-%{version}
%endif
