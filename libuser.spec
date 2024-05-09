#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : libuser
Version  : 0.64
Release  : 44
URL      : https://releases.pagure.org/libuser/libuser-0.64.tar.gz
Source0  : https://releases.pagure.org/libuser/libuser-0.64.tar.gz
Summary  : A user and group account administration library.
Group    : Development/Tools
License  : LGPL-2.0
Requires: libuser-bin = %{version}-%{release}
Requires: libuser-lib = %{version}-%{release}
Requires: libuser-license = %{version}-%{release}
Requires: libuser-locales = %{version}-%{release}
Requires: libuser-man = %{version}-%{release}
Requires: libuser-python = %{version}-%{release}
Requires: libuser-python3 = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : file
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-no-export-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : popt-dev
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Disable-docs.patch

%description
About
=====
The libuser library implements a standardized interface for manipulating and
administering user and group accounts.  The library uses pluggable back-ends to
interface to its data sources.

%package bin
Summary: bin components for the libuser package.
Group: Binaries
Requires: libuser-license = %{version}-%{release}

%description bin
bin components for the libuser package.


%package dev
Summary: dev components for the libuser package.
Group: Development
Requires: libuser-lib = %{version}-%{release}
Requires: libuser-bin = %{version}-%{release}
Provides: libuser-devel = %{version}-%{release}
Requires: libuser = %{version}-%{release}

%description dev
dev components for the libuser package.


%package lib
Summary: lib components for the libuser package.
Group: Libraries
Requires: libuser-license = %{version}-%{release}

%description lib
lib components for the libuser package.


%package license
Summary: license components for the libuser package.
Group: Default

%description license
license components for the libuser package.


%package locales
Summary: locales components for the libuser package.
Group: Default

%description locales
locales components for the libuser package.


%package man
Summary: man components for the libuser package.
Group: Default

%description man
man components for the libuser package.


%package python
Summary: python components for the libuser package.
Group: Default
Requires: libuser-python3 = %{version}-%{release}

%description python
python components for the libuser package.


%package python3
Summary: python3 components for the libuser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libuser package.


%prep
%setup -q -n libuser-0.64
cd %{_builddir}/libuser-0.64
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715291437
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static --disable-gtk-doc \
--disable-gtk-doc-html \
--disable-rpath
make

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1715291437
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuser
cp %{_builddir}/libuser-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libuser/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
%find_lang libuser

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lchage
/usr/bin/lchfn
/usr/bin/lchsh
/usr/bin/lgroupadd
/usr/bin/lgroupdel
/usr/bin/lgroupmod
/usr/bin/lid
/usr/bin/lnewusers
/usr/bin/lpasswd
/usr/bin/luseradd
/usr/bin/luserdel
/usr/bin/lusermod

%files dev
%defattr(-,root,root,-)
/usr/include/libuser/config.h
/usr/include/libuser/entity.h
/usr/include/libuser/error.h
/usr/include/libuser/fs.h
/usr/include/libuser/prompt.h
/usr/include/libuser/user.h
/usr/include/libuser/user_private.h
/usr/lib64/libuser.so
/usr/lib64/pkgconfig/libuser.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuser.so.1
/usr/lib64/libuser.so.1.5.2
/usr/lib64/libuser/libuser_files.so
/usr/lib64/libuser/libuser_shadow.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuser/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lchage.1
/usr/share/man/man1/lchfn.1
/usr/share/man/man1/lchsh.1
/usr/share/man/man1/lgroupadd.1
/usr/share/man/man1/lgroupdel.1
/usr/share/man/man1/lgroupmod.1
/usr/share/man/man1/lid.1
/usr/share/man/man1/lnewusers.1
/usr/share/man/man1/lpasswd.1
/usr/share/man/man1/luseradd.1
/usr/share/man/man1/luserdel.1
/usr/share/man/man1/lusermod.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libuser.lang
%defattr(-,root,root,-)

