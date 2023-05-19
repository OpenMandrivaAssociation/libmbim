%define major 4
%define libname %mklibname mbim-glib %{major}
%define devname %mklibname mbim-glib -d

Summary:	MBIM modem protocol helper library
Name:		libmbim
Version:	1.28.4
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/libmbim/libmbim/
Source0:	https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/%{version}/libmbim-%{version}.tar.bz2	
#Source0:	http://www.freedesktop.org/software/libmbim/libmbim-%version.tar.xz
BuildRequires:	meson
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	autoconf-archive
BuildRequires:	gtk-doc

%description
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		Development/C

%description -n %{libname}
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM shared libraries.

%files -n %{libname}
%doc AUTHORS NEWS
%{_libdir}/libmbim-glib.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and development libraries for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.

This package contains MBIM header files and development libraries.

%files -n %{devname}
%dir %{_includedir}/libmbim-glib
%{_includedir}/libmbim-glib/*.h
%{_libdir}/libmbim-glib.so
%{_libdir}/pkgconfig/mbim-glib.pc
%{_datadir}/gtk-doc/html/*

#----------------------------------------------------------------------------
%package gir
Summary:        GObject Introspection interface to libmbim
Group:          Development/C
Requires:       %{libname} = %{version}
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description gir
GObject Introspection interface to libmbim

%files gir
%{_libdir}/girepository-1.0/Mbim-1.0.typelib
%{_datadir}/gir-1.0/Mbim-1.0.gir

#----------------------------------------------------------------------------

%package utils
Summary:	MBIM command line utilities
Group:		System/Base

%description utils
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.

This package contains MBIM command line utilities.

%files utils
%{_bindir}/mbim-network
%{_bindir}/mbimcli
%{_datadir}/bash-completion/completions/mbimcli
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim-network.1*
%{_mandir}/man1/mbimcli.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson \
        -Dgtk_doc=true

%meson_build

%install
%meson_install
