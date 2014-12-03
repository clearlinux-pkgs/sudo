#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sudo
Version  : 1.8.14p3
Release  : 25
URL      : http://www.sudo.ws/dist/sudo-1.8.14p3.tar.gz
Source0  : http://www.sudo.ws/dist/sudo-1.8.14p3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC MIT-Opengroup
Requires: sudo-setuid
Requires: sudo-bin
Requires: sudo-data
Requires: sudo-doc
Requires: sudo-locales
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : zlib-dev
Patch1: stateless.patch
Patch2: 0001-Add-read-only-sudoers.d-dir.patch
Patch3: 0001-visudo-Use-sane-default-file.patch

%description
The sudo philosophy
===================
Sudo is a program designed to allow a sysadmin to give limited root privileges
to users and log root activity.  The basic philosophy is to give as few
privileges as possible but still allow people to get their work done.

%package bin
Summary: bin components for the sudo package.
Group: Binaries
Requires: sudo-data
Requires: sudo-setuid

%description bin
bin components for the sudo package.


%package data
Summary: data components for the sudo package.
Group: Data

%description data
data components for the sudo package.


%package dev
Summary: dev components for the sudo package.
Group: Development
Requires: sudo-bin
Requires: sudo-data

%description dev
dev components for the sudo package.


%package doc
Summary: doc components for the sudo package.
Group: Documentation

%description doc
doc components for the sudo package.


%package locales
Summary: locales components for the sudo package.
Group: Default

%description locales
locales components for the sudo package.


%package setuid
Summary: setuid components for the sudo package.
Group: Default

%description setuid
setuid components for the sudo package.


%prep
%setup -q -n sudo-1.8.14p3
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%reconfigure --disable-static --with-pam \
--with-env-editor \
--with-ignore-dot \
--with-tty-tickets
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check || :

%install
rm -rf %{buildroot}
%make_install INSTALL_OWNER=""
%find_lang sudo
%find_lang sudoers

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sudo
/usr/bin/sudoedit
/usr/bin/sudoreplay
/usr/bin/visudo
/usr/libexec/sudo/group_file.so
/usr/libexec/sudo/libsudo_util.so
/usr/libexec/sudo/libsudo_util.so.0
/usr/libexec/sudo/libsudo_util.so.0.0.0
/usr/libexec/sudo/sudo_noexec.so
/usr/libexec/sudo/sudoers.so
/usr/libexec/sudo/system_group.so

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sudo/sudoers

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/sudo/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/sudo

%files locales -f sudo.lang -f sudoers.lang 
%defattr(-,root,root,-)

