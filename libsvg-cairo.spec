Summary:	SVG rendering using Cairo
Summary(pl):	Renderowanie SVG przy u¿yciu Cairo
Name:		libsvg-cairo
Version:	0.1.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	5e0bbae11601c4d7884ceeb364d52a84
URL:		http://www.xsvg.org/
BuildRequires:	cairo-devel >= 0.1.8
BuildRequires:	libsvg-devel >= 0.1.0
BuildRequires:	pkgconfig
Requires:	cairo >= 0.1.8
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
Requires:	%{name} = %{version}
Requires:	cairo-devel >= 0.1.8
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
Requires:	%{name}-devel = %{version}
Obsoletes:	libxsvg-static

%description static
Static libxsvg library.

%description static -l pl
Statyczna biblioteka libxsvg.

%prep
%setup -q

%build
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
%doc AUTHORS COPYING ChangeLog NEWS README
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
