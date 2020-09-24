#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA9F4C021CEA470FB (Todd.Miller@sudo.ws)
#
Name     : sudo
Version  : 1.9.3
Release  : 70
URL      : https://www.sudo.ws/dist/sudo-1.9.3.tar.gz
Source0  : https://www.sudo.ws/dist/sudo-1.9.3.tar.gz
Source1  : https://www.sudo.ws/dist/sudo-1.9.3.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: sudo-bin = %{version}-%{release}
Requires: sudo-data = %{version}-%{release}
Requires: sudo-libexec = %{version}-%{release}
Requires: sudo-locales = %{version}-%{release}
Requires: sudo-man = %{version}-%{release}
Requires: sudo-setuid = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : groff
BuildRequires : zlib-dev
Patch1: 0001-stateless.patch
Patch2: 0002-Add-read-only-sudoers.d-dir.patch
Patch3: 0003-visudo-Use-sane-default-file.patch
Patch4: 0004-man-pages-add-stateless-locations.patch
Patch5: 0005-keep-proxy-settings-environment-variables.patch

%description
The sudo philosophy
===================
Sudo is a program designed to allow a sysadmin to give limited root privileges
to users and log root activity.  The basic philosophy is to give as few
privileges as possible but still allow people to get their work done.

%package bin
Summary: bin components for the sudo package.
Group: Binaries
Requires: sudo-data = %{version}-%{release}
Requires: sudo-libexec = %{version}-%{release}
Requires: sudo-setuid = %{version}-%{release}

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
Requires: sudo-bin = %{version}-%{release}
Requires: sudo-data = %{version}-%{release}
Provides: sudo-devel = %{version}-%{release}
Requires: sudo = %{version}-%{release}

%description dev
dev components for the sudo package.


%package doc
Summary: doc components for the sudo package.
Group: Documentation
Requires: sudo-man = %{version}-%{release}

%description doc
doc components for the sudo package.


%package libexec
Summary: libexec components for the sudo package.
Group: Default

%description libexec
libexec components for the sudo package.


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
%setup -q -n sudo-1.9.3
cd %{_builddir}/sudo-1.9.3
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600983626
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-pam \
--with-env-editor \
--with-ignore-dot \
--with-tty-tickets \
--with-editor=/usr/bin/vim:/usr/bin/vi:/usr/bin/nano
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1600983626
rm -rf %{buildroot}
%make_install INSTALL_OWNER=""
%find_lang sudo
%find_lang sudoers
## install_append content
rm -rfv %{buildroot}/etc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cvtsudoers
/usr/bin/sudo_logsrvd
/usr/bin/sudo_sendlog
/usr/bin/sudoedit
/usr/bin/sudoreplay
/usr/bin/visudo

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sudo/sudoers

%files dev
%defattr(-,root,root,-)
/usr/include/sudo_plugin.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/sudo/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/sudo/audit_json.so
/usr/libexec/sudo/group_file.so
/usr/libexec/sudo/libsudo_util.so
/usr/libexec/sudo/libsudo_util.so.0
/usr/libexec/sudo/libsudo_util.so.0.0.0
/usr/libexec/sudo/sample_approval.so
/usr/libexec/sudo/sudo_noexec.so
/usr/libexec/sudo/sudoers.so
/usr/libexec/sudo/system_group.so

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cvtsudoers.1
/usr/share/man/man5/sudo.conf.5
/usr/share/man/man5/sudo_logsrv.proto.5
/usr/share/man/man5/sudo_logsrvd.conf.5
/usr/share/man/man5/sudoers.5
/usr/share/man/man5/sudoers_timestamp.5
/usr/share/man/man8/sudo.8
/usr/share/man/man8/sudo_logsrvd.8
/usr/share/man/man8/sudo_plugin.8
/usr/share/man/man8/sudo_sendlog.8
/usr/share/man/man8/sudoedit.8
/usr/share/man/man8/sudoreplay.8
/usr/share/man/man8/visudo.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/sudo

%files locales -f sudo.lang -f sudoers.lang
%defattr(-,root,root,-)

