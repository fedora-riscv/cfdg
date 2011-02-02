Name: cfdg
Version:  2.2.2
Release:  1%{?dist}
Summary: Context Free Design Grammar

Group: Amusements/Games 
License: GPLv2+
URL: http://www.contextfreeart.org/

#Source0: ContextFreeSource%{version}.tar.gz
Source0: http://www.contextfreeart.org/download/ContextFreeSource%{version}.tgz
#Modified tarball due to licensing issues, to be fixed in 2.2
#To create from upstream:
#gunzip ContextFreeSource2.1.tgz
#tar -xf ContextFreeSource2.1.tar
#rm ContextFreeSource2.1/src-common/test.cpp 
#rm ContextFreeSource2.1/src-common/test.h
#rm ContextFreeSource2.1/src-common/test-test.cpp 
#tar -cf ContextFreeSource2.1.tar ContextFreeSource2.1
#gzip ContextFreeSource2.1.tar

#GCC 4.3 compatibility patches.  Submitted upstream via email 2008-06-25.
#Patch0: contextfree-2.1-builder-includes.patch
#Patch1: contextfree-2.1-yglue-includes.patch
#Patch2: contextfree-2.1-SVGCanvas-includes.patch
#Patch3: contextfree-2.1-tiledCanvas-includes.patch
#Patch4: contextfree-2.1-posixSystem-includes.patch
#Strip patch.
Patch5: contextfree-2.1-Makefile-nostrip.patch
Patch6: contextfree-2.2-mktemp.patch
Patch7: contextfree-2.2-optflags.patch
Patch8: contextfree-2.2.1-dsolink.patch
Patch9: contextfree-2.2.2-yglue-type-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root%(%{__id_u} -n)
BuildRequires: libpng-devel, byacc, flex

%description
Context Free is a program that generates images from written instructions 
called a grammar. The program follows the instructions in a few seconds to 
create images that can contain millions of shapes.

%prep
%setup -qn ContextFreeSource%{version}.tgz

#%patch0 -p0
#%patch1 -p0
#%patch2 -p0
#%patch3 -p0
#%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0

%build

make OPTFLAGS='%{optflags}' %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 755 cfdg %{buildroot}%{_bindir}/cfdg

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/cfdg
%doc input/* LICENSE.txt README.txt

%changelog
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
