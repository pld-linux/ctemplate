#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Simple and powerful template language for C++
Name:		ctemplate
Version:	2.2
Release:	1
License:	BSD
Group:		Applications
# Google Code no longer provides downloads for projects, upstream
# refuses to use Google Drive, they ask users to fetch from svn repository by themselves.
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/ctemplate/%{name}-%{version}.tar.gz/1de89d9073f473c1e31862c4581636f3/ctemplate-%{version}.tar.gz
# Source0-md5:	1de89d9073f473c1e31862c4581636f3
URL:		http://code.google.com/p/google-ctemplate/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
export PTHREAD_LIBS="-lpthread"
%configure \
	--disable-silent-rules
%{__make}
%{?with_test:%{__make} check}

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

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libctemplate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libctemplate.so.2
%attr(755,root,root) %{_libdir}/libctemplate_nothreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libctemplate_nothreads.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libctemplate.so
%{_libdir}/libctemplate_nothreads.so
%{_libdir}/libctemplate.la
%{_libdir}/libctemplate_nothreads.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_pkgconfigdir}/libctemplate.pc
%{_pkgconfigdir}/libctemplate_nothreads.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libctemplate.a
%{_libdir}/libctemplate_nothreads.a

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/*
