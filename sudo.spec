#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA9F4C021CEA470FB (Todd.Miller@sudo.ws)
#
Name     : sudo
Version  : 1.8.24
Release  : 56
URL      : https://www.sudo.ws/dist/sudo-1.8.24.tar.gz
Source0  : https://www.sudo.ws/dist/sudo-1.8.24.tar.gz
Source99 : https://www.sudo.ws/dist/sudo-1.8.24.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: sudo-bin
Requires: sudo-setuid
Requires: sudo-data
Requires: sudo-license
Requires: sudo-locales
Requires: sudo-man
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : groff
BuildRequires : zlib-dev
Patch1: 0001-stateless.patch
Patch2: 0002-Add-read-only-sudoers.d-dir.patch
Patch3: 0003-visudo-Use-sane-default-file.patch
Patch4: 0004-man-pages-add-stateless-locations.patch

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
Requires: sudo-license
Requires: sudo-man

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
Provides: sudo-devel

%description dev
dev components for the sudo package.


%package doc
Summary: doc components for the sudo package.
Group: Documentation
Requires: sudo-man

%description doc
doc components for the sudo package.


%package license
Summary: license components for the sudo package.
Group: Default

%description license
license components for the sudo package.


%package locales
Summary: locales components for the sudo package.
Group: Default

%description locales
locales components for the sudo package.


%package man
Summary: man components for the sudo package.
Group: Default

%description man
man components for the sudo package.


%package setuid
Summary: setuid components for the sudo package.
Group: Default

%description setuid
setuid components for the sudo package.


%prep
%setup -q -n sudo-1.8.24
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534609639
%configure --disable-static --with-pam \
--with-env-editor \
--with-ignore-dot \
--with-tty-tickets
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1534609639
rm -rf %{buildroot}
%make_install INSTALL_OWNER=""
%find_lang sudo
%find_lang sudoers

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sudo
/usr/bin/cvtsudoers
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
/usr/share/defaults/sudo/sudoers.dist

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/sudo/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/sudo/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/cvtsudoers.1
/usr/share/man/man5/sudo.conf.5
/usr/share/man/man5/sudoers.5
/usr/share/man/man5/sudoers_timestamp.5
/usr/share/man/man8/sudo.8
/usr/share/man/man8/sudo_plugin.8
/usr/share/man/man8/sudoedit.8
/usr/share/man/man8/sudoreplay.8
/usr/share/man/man8/visudo.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/sudo

%files locales -f sudo.lang -f sudoers.lang
%defattr(-,root,root,-)

