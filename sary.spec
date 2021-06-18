Summary: sary is a suffix array library.
Name: sary
Version: 1.2.0
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.gz
URL: http://sary.namazu.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: glib >= 1.2.4

%description
Sary is a suffix array library.  It provides fast full-text
search facilities for huge, say, 10 MB, 100 MB text files.

%package devel
Summary: Libraries and include files of sary
Group: Development/Libraries
Requires: %name = %{version}

%description devel
Libraries and include files of sary.

%changelog
* Wed Jun 06 2001 Ryuji Abe <rug@namazu.org>
- added sary.pc

* Thu May 31 2001 Ryuji Abe <rug@namazu.org>
- more macros

* Tue Dec 01 2000 Satoru Takabayashi <satoru@namazu.org>
- Fix %files for recent updates.

* Tue Nov 21 2000 Ryuji Abe <rug@namazu.org>
- Fix %files for recent updates.
- Fix URL.

* Mon Nov 06 2000 Satoru Takabayashi <satoru@namazu.org>
- Initial version.

%prep 
%setup -q

%build
%configure

if [ "$SMP" != "" ]; then
  make -j$SMP "MAKE=make -j$SMP"
else
  make
fi

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING INSTALL README NEWS
%{_bindir}/sary
%{_bindir}/mksary
%{_datadir}/sary/docs/*
%{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_bindir}/sary-config
%{_includedir}/sary.h
%{_includedir}/sary/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*a
%{_libdir}/pkgconfig/sary.pc
%{_datadir}/aclocal/sary.m4
