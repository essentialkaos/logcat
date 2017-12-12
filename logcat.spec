########################################################################################

%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock

%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include

########################################################################################

Summary:            Utility for log viewing with additional access control mechanism
Name:               logcat
Version:            2.1.3
Release:            0%{?dist}
License:            EKOL
Group:              Applications/System
URL:                https://github.com/essentialkaos/logcat

Source0:            https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:           %{name} = %{version}-%{release}

########################################################################################

%description
Utility for log viewing with additional access control mechanism (for sudo logcat).

########################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}

install -pm 755 %{name} %{buildroot}%{_bindir}/%{name}
install -pm 644 %{name}.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

########################################################################################

%files
%defattr(-, root, root, -)
%doc LICENSE.EN LICENSE.RU
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}

########################################################################################

%changelog
* Tue Dec 12 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.3-0
- Code refactoring

* Tue Oct 10 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.1-0
- Fixed bug with reading files with a+r permissions (readable for all)

* Mon Sep 25 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.0-0
- Code refactoring

* Mon Apr 24 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.2-0
- Arguments parser updated to v3 with fixed stderr output redirection for
  showArgWarn and showArgValWarn functions

* Wed Apr 05 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.1-0
- Output errors to stderr

* Mon Feb 20 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.0-0
- Added support of reading non-root owned files (if user has sufficient privileges)
- Overall improvements
- Grammar fixes

* Wed Nov 16 2016 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Code refactoring

* Mon Oct 31 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.3-0
- Fixed bug with arguments parsing

* Sun Oct 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.2-0
- UI improvements

* Sat Jan 16 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Removed shenx usage
- Minor improvements

* Tue Oct 28 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Improved grep speed
- Separated grep and egrep usage
- Small fixes

* Fri Mar 21 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-1
- Fixed major bug with config rewriting
