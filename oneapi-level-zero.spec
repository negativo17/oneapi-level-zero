## START: Set by rpmautospec
## (rpmautospec version 0.3.1)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

%global         srcname level-zero
Name:           oneapi-%{srcname}
Version:        1.9.4
Release:        %{autorelease}
Summary:        OneAPI Level Zero Specification Headers and Loader

License:        MIT
URL:            https://github.com/oneapi-src/%{srcname}
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake3
BuildRequires:  devtoolset-9-gcc-c++
BuildRequires:  make
BuildRequires:  opencl-headers

%description
The objective of the oneAPI Level-Zero Application Programming Interface
(API) is to provide direct-to-metal interfaces to offload accelerator
devices. Its programming interface can be tailored to any device needs
and can be adapted to support broader set of languages features such as
function pointers, virtual functions, unified memory,
and I/O capabilities.

%package        devel
Summary:        The oneAPI Level Zero Specification Headers and Loader development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
. /opt/rh/devtoolset-9/enable
%cmake3
%cmake3_build

%install
%cmake3_install

%files
%license LICENSE
%doc README.md SECURITY.md
%{_libdir}/libze_loader.so.1*
%{_libdir}/libze_validation_layer.so.1*
%{_libdir}/libze_tracing_layer.so.1*

%files devel
%{_includedir}/level_zero
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/pkgconfig/libze_loader.pc
%{_libdir}/pkgconfig/%{srcname}.pc

%changelog
* Fri Jan 20 2023 František Zatloukal <fzatlouk@redhat.com> - 1.9.4-1
- Release 1.9.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 František Zatloukal <fzatlouk@redhat.com> - 1.8.12-1
- Release 1.8.12

* Mon Dec 12 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 1.8.8-1
- New package
