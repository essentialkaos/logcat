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

Summary:            Utility for controllable log viewing with sudo
Name:               logcat
Version:            1.3.1
Release:            0%{?dist}
License:            EKOL
Group:              Applications/System
URL:                http://essentialkaos.com

Source0:            https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:           %{name} = %{version}-%{release}

########################################################################################

%description
Some system log can be viewed only with root priveleges. This is utility is proxy
for viewing some logs with using sudo command.

########################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_sbindir}
install -dm 755 %{buildroot}%{_sysconfdir}

install -pm 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -pm 600 %{name}.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

########################################################################################

%files
%defattr(-, root, root, -)
%doc LICENSE.EN LICENSE.RU
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}

########################################################################################

%changelog
* Sat Jan 16 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Removed shenx usage
- Minor improvements

* Tue Oct 28 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Improved grep speed
- Separated grep and egrep usage
- Small fixes

* Fri Mar 21 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-1
- Fixed major bug with config rewriting
