Summary:	SVG rendering using Cairo
Summary(pl):	Renderowanie SVG przy u¿yciu Cairo
Name:		libsvg-cairo
Version:	0.1.6
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	d79da7b3a60ad8c8e4b902c9b3563047
URL:		http://www.xsvg.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	libsvg-devel >= 0.1.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	cairo >= 0.5.0
Requires:	libsvg >= 0.1.2
Obsoletes:	libxsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxsvg provides the ability to render SVG content from files or
buffers. All rendering is performed using the Cairo rendering library
(formerly called Xr).

%description -l pl
libxsvg daje mo¿liwo¶æ renderowania danych SVG z plików lub buforów.
Ca³o¶æ renderowania jest wykonywana przy u¿yciu biblioteki
renderuj±cej Cairo (dawniej nazywanej Xr).

%package devel
Summary:	Header files for libxsvg library
Summary(pl):	Pliki nag³ówkowe biblioteki libxsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 0.5.0
Requires:	libsvg-devel >= 0.1.2
Obsoletes:	libxsvg-devel

%description devel
Header files for libxsvg library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxsvg.

%package static
Summary:	Static libxsvg library
Summary(pl):	Statyczna biblioteka libxsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxsvg-static

%description static
Static libxsvg library.

%description static -l pl
Statyczna biblioteka libxsvg.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
