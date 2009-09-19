Summary:	Simple and powerful template language for C++
Name:		ctemplate
Version:	0.95
Release:	1
License:	BSD
Group:		Applications
Source0:	http://google-ctemplate.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	d6cfabbe1742dbe6f3bd10b77be319f1
URL:		http://code.google.com/p/google-ctemplate/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CTemplate is a simple and powerful template language for C++. It
emphasizes separating logic from presentation: it is impossible to
embed application logic in this template language.

%package libs
Summary:	CTemplate library
Summary(pl.UTF-8):	Biblioteka CTemplate
Group:		Libraries

%description libs
This package contains CTemplate library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę CTemplate.

%package doc
Summary:	CTemplate documentation
Summary(pl.UTF-8):	Dokumentacja CTemplate
Group:		Development/Libraries

%description doc
CTemplate documentation.

%description doc -l pl.UTF-8
Dokumentacja CTemplate.

%package devel
Summary:	Header files for CTemplate
Summary(pl.UTF-8):	Pliki nagłówkowe CTemplate
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for CTemplate.

%description devel -l pl.UTF-8
Pliki nagłówkowe CTemplate.

%package static
Summary:	Static CTemplate library
Summary(pl.UTF-8):	Statyczna biblioteka CTemplate
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static CTemplate library.

%description static -l pl.UTF-8
Statyczna biblioteka CTemplate.


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

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/diff_tpl_auto_escape
%attr(755,root,root) %{_bindir}/make_tpl_varnames_h
%attr(755,root,root) %{_bindir}/template-converter

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libctemplate*.so
%attr(755,root,root) %{_libdir}/libctemplate*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libctemplate*.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libctemplate*.so.?

%files static
%defattr(644,root,root,755)
%{_libdir}/libctemplate*.a
