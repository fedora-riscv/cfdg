Name: cfdg
Version:  3.0
Release:  0.beta2%{?dist}.14
Summary: Context Free Design Grammar

Group: Amusements/Games 
License: GPLv2+
URL: http://www.contextfreeart.org/

Source0: http://www.contextfreeart.org/download/ContextFreeSource3.0beta2.tgz

#GCC 4.3 compatibility patches.  Submitted upstream via email 2008-06-25.
#Patch0: contextfree-2.1-builder-includes.patch
#Patch1: contextfree-2.1-yglue-includes.patch
#Patch2: contextfree-2.1-SVGCanvas-includes.patch
#Patch3: contextfree-2.1-tiledCanvas-includes.patch
#Patch4: contextfree-2.1-posixSystem-includes.patch
#Strip patch.
Patch5: contextfree-2.1-Makefile-nostrip.patch
Patch6: contextfree-2.2-mktemp.patch
#Patch7: contextfree-2.2-optflags.patch
Patch8: contextfree-2.2.1-dsolink.patch
#Patch9: contextfree-2.2.2-yglue-type-fix.patch
Patch10: contextfree-3.0-optflags.patch
BuildRequires: libpng-devel, bison, flex

%description
Context Free is a program that generates images from written instructions 
called a grammar. The program follows the instructions in a few seconds to 
create images that can contain millions of shapes.

%prep
%setup -qn ContextFreeSource3.0beta2

#%patch0 -p0
#%patch1 -p0
#%patch2 -p0
#%patch3 -p0
#%patch4 -p0
%patch5 -p0
%patch6 -p0
#%patch7 -p0
%patch8 -p0
#%patch9 -p0
%patch10 -p0

%build

OPTFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 755 cfdg %{buildroot}%{_bindir}/cfdg


%files
%{_bindir}/cfdg
%doc input/* LICENSE.txt README.txt

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0-0.beta2.7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jon Ciesla <limburgher@gmail.com> - 3.0-0.beta2.1
- Fix optflags, BZ 795104.

* Fri Feb 17 2012 Jon Ciesla <limburgher@gmail.com> - 3.0-0.beta2
- New upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 2.2.2-3
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Jon Ciesla <limb@jcomserv.net> - 2.2.2-1
- New upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 2.2.1-2
- Fix for FTBFS, BZ 600013.

* Mon Oct 05 2009 Jon Ciesla <limb@jcomserv.net> - 2.2.1-1
- New upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Jon Ciesla <limb@jcomserv.net> - 2.2-3
- Rebuild due to 505774.

* Fri Jun 12 2009 Ville Skyttä <ville.skytta at iki.fi> - 2.2-2
- Build with %%{optflags}.

* Mon Apr 27 2009 Jon Ciesla <limb@jcomserv.net> - 2.2-1
- 2.2, fixed licencing and gcc issues.
- Updated mktemp, optflag patches.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 24 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-5
- Created modified tarball for licensing issue.

* Wed Oct 15 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-4
- Optflag fix.
- Added smp flags.
- Simplified install process.
- Retconned initial changelog entry.
- Fixed URL.

* Tue Oct 14 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-3
- Patched for mktemp error.

* Mon Aug 18 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-2
- Annotated patches, append CFLAGS for review.

* Tue Jun 17 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-1
- Create.
