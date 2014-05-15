%define major 0
%define libname %mklibname mbim-glib %{major}
%define devname %mklibname mbim-glib -d

Summary:	MBIM modem protocol helper library
Name:		libmbim
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/libmbim/libmbim/
Source0:	http://www.freedesktop.org/software/libmbim/libmbim-%version.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	gtk-doc

%description
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		Development/C

%description -n	%{libname}
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM shared libraries.

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/libmbim-glib.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Header files and development libraries for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
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
%{_mandir}/man1/mbim-network.1.*
%{_mandir}/man1/mbimcli.1.*
#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc
%make

%install
%makeinstall_std

%check
make check

