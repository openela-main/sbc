Name:          sbc
Version:       1.4
Release:       9%{?dist}
Summary:       Sub Band Codec used by bluetooth A2DP

License:       GPLv2 and LGPLv2+
URL:           http://www.bluez.org
Source0:       http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libsndfile-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
SBC (Sub Band Codec) is a low-complexity audio codec used in the Advanced Audio 
Distribution Profile (A2DP) bluetooth standard but can be used standalone. It 
uses 4 or 8 subbands, an adaptive bit allocation algorithm in combination with 
an adaptive block PCM quantizers.

%package -n libsbc
Summary: Library for the SBC (Sub Band Codec)

%description -n libsbc
Library for SBC (Sub Band Codec) is a low-complexity audio codec used in the
Advanced Audio Distribution Profile (A2DP) bluetooth standard but can be used
standalone. It uses 4 or 8 subbands, an adaptive bit allocation algorithm in
combination with an adaptive block PCM quantizers.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q

%build
%configure --disable-static

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog
%{_bindir}/sbc*

%files -n libsbc
%license COPYING
%{_libdir}/libsbc.so.1*

%files devel
%{_includedir}/sbc/
%{_libdir}/pkgconfig/sbc.pc
%{_libdir}/libsbc.so

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.4-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.4-8
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-4
- Split library out to sub package

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-1
- Update to 1.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-9
- Add gcc BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-2
- Use %%license

* Thu Nov 20 2014 Bastien Nocera <bnocera@redhat.com> 1.3-1
- Update to 1.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Bastien Nocera <bnocera@redhat.com> 1.2-1
- Update to 1.2

* Sat Aug 24 2013 Bastien Nocera <bnocera@redhat.com> 1.1-1
- Update to 1.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0-2
- track lib soname, minor .spec cleanup

* Sat Dec  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-1
- Initial package
