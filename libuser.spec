#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuser
Version  : 0.62
Release  : 12
URL      : http://releases.pagure.org/libuser/libuser-0.62.tar.xz
Source0  : http://releases.pagure.org/libuser/libuser-0.62.tar.xz
Summary  : A user and group account administration library.
Group    : Development/Tools
License  : LGPL-2.0
Requires: libuser-bin
Requires: libuser-legacypython
Requires: libuser-lib
Requires: libuser-doc
Requires: libuser-locales
Requires: libuser-python
BuildRequires : Linux-PAM-dev
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-no-export-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : popt-dev
BuildRequires : python-dev
BuildRequires : python3-dev

%description
About
=====
The libuser library implements a standardized interface for manipulating and
administering user and group accounts.  The library uses pluggable back-ends to
interface to its data sources.

%package bin
Summary: bin components for the libuser package.
Group: Binaries

%description bin
bin components for the libuser package.


%package dev
Summary: dev components for the libuser package.
Group: Development
Requires: libuser-lib
Requires: libuser-bin
Provides: libuser-devel

%description dev
dev components for the libuser package.


%package doc
Summary: doc components for the libuser package.
Group: Documentation

%description doc
doc components for the libuser package.


%package legacypython
Summary: legacypython components for the libuser package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the libuser package.


%package lib
Summary: lib components for the libuser package.
Group: Libraries

%description lib
lib components for the libuser package.


%package locales
Summary: locales components for the libuser package.
Group: Default

%description locales
locales components for the libuser package.


%package python
Summary: python components for the libuser package.
Group: Default
Requires: libuser-legacypython

%description python
python components for the libuser package.


%prep
%setup -q -n libuser-0.62

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517941802
%configure --disable-static --disable-gtk-doc-html PYTHON=python2
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517941802
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
/usr/share/gtk-doc/html/libuser/api-index-full.html
/usr/share/gtk-doc/html/libuser/ch01.html
/usr/share/gtk-doc/html/libuser/deprecated-api-index.html
/usr/share/gtk-doc/html/libuser/home.png
/usr/share/gtk-doc/html/libuser/index.html
/usr/share/gtk-doc/html/libuser/index.sgml
/usr/share/gtk-doc/html/libuser/left-insensitive.png
/usr/share/gtk-doc/html/libuser/left.png
/usr/share/gtk-doc/html/libuser/libuser-config.html
/usr/share/gtk-doc/html/libuser/libuser-entity.html
/usr/share/gtk-doc/html/libuser/libuser-error.html
/usr/share/gtk-doc/html/libuser/libuser-fs.html
/usr/share/gtk-doc/html/libuser/libuser-prompt.html
/usr/share/gtk-doc/html/libuser/libuser-user.html
/usr/share/gtk-doc/html/libuser/libuser-value.html
/usr/share/gtk-doc/html/libuser/libuser.devhelp2
/usr/share/gtk-doc/html/libuser/right-insensitive.png
/usr/share/gtk-doc/html/libuser/right.png
/usr/share/gtk-doc/html/libuser/style.css
/usr/share/gtk-doc/html/libuser/up-insensitive.png
/usr/share/gtk-doc/html/libuser/up.png

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuser.so.1
/usr/lib64/libuser.so.1.5.2
/usr/lib64/libuser/libuser_files.so
/usr/lib64/libuser/libuser_shadow.so

%files python
%defattr(-,root,root,-)

%files locales -f libuser.lang
%defattr(-,root,root,-)

