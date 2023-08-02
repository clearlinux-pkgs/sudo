#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xA9F4C021CEA470FB (Todd.Miller@sudo.ws)
#
Name     : sudo
Version  : 1.9.14p3
Release  : 94
URL      : https://www.sudo.ws/dist/sudo-1.9.14p3.tar.gz
Source0  : https://www.sudo.ws/dist/sudo-1.9.14p3.tar.gz
Source1  : https://www.sudo.ws/dist/sudo-1.9.14p3.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause ISC
Requires: sudo-bin = %{version}-%{release}
Requires: sudo-libexec = %{version}-%{release}
Requires: sudo-license = %{version}-%{release}
Requires: sudo-locales = %{version}-%{release}
Requires: sudo-man = %{version}-%{release}
Requires: sudo-setuid = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : groff
BuildRequires : openssl-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-new-sudoer-group-role.patch
Patch2: 0002-keep-proxy-settings-environment-variables.patch

%description
NLS Translations for sudo are coordinated through the Translation
Project, at https://translationproject.org/

%package bin
Summary: bin components for the sudo package.
Group: Binaries
Requires: sudo-libexec = %{version}-%{release}
Requires: sudo-setuid = %{version}-%{release}
Requires: sudo-license = %{version}-%{release}

%description bin
bin components for the sudo package.


%package dev
Summary: dev components for the sudo package.
Group: Development
Requires: sudo-bin = %{version}-%{release}
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
Requires: sudo-license = %{version}-%{release}

%description libexec
libexec components for the sudo package.


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
%setup -q -n sudo-1.9.14p3
cd %{_builddir}/sudo-1.9.14p3
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690939201
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-pam \
--with-env-editor \
--with-ignore-dot \
--with-tty-tickets \
--with-editor=/usr/bin/vim:/usr/bin/vi:/usr/bin/nano \
--with-all-insults
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1690939201
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sudo
cp %{_builddir}/sudo-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/sudo/c2ba3629efe22105261b63be3019a3f60be20a5a || :
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

%files dev
%defattr(-,root,root,-)
/usr/include/sudo_plugin.h

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/sudo/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/sudo/audit_json.so
/usr/libexec/sudo/group_file.so
/usr/libexec/sudo/libsudo_util.so
/usr/libexec/sudo/libsudo_util.so.0
/usr/libexec/sudo/libsudo_util.so.0.0.0
/usr/libexec/sudo/sudo_intercept.so
/usr/libexec/sudo/sudo_noexec.so
/usr/libexec/sudo/sudoers.so
/usr/libexec/sudo/system_group.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sudo/c2ba3629efe22105261b63be3019a3f60be20a5a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cvtsudoers.1
/usr/share/man/man5/sudo.conf.5
/usr/share/man/man5/sudo_logsrv.proto.5
/usr/share/man/man5/sudo_logsrvd.conf.5
/usr/share/man/man5/sudo_plugin.5
/usr/share/man/man5/sudoers.5
/usr/share/man/man5/sudoers_timestamp.5
/usr/share/man/man8/sudo.8
/usr/share/man/man8/sudo_logsrvd.8
/usr/share/man/man8/sudo_sendlog.8
/usr/share/man/man8/sudoedit.8
/usr/share/man/man8/sudoreplay.8
/usr/share/man/man8/visudo.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/sudo

%files locales -f sudo.lang -f sudoers.lang
%defattr(-,root,root,-)

