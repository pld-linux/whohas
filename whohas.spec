Summary:	whohas is a command line tool that allows querying several package lists at once
Summary(hu.UTF-8):	whohas egy parancssoros eszköz, amellyel különböző csomaglistákat kérhetsz le egyszerre
Name:		whohas
Version:	0.23
Release:	0.1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.philippwesche.org/200811/whohas/%{name}-%{version}.tar.gz
# Source0-md5:	0895fb6353950fe2e686fa867aaf0416
URL:		http://www.philippwesche.org/200811/whohas/intro.html
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
whohas is a command line tool that allows querying several package
lists at once - currently supported are Arch, Debian, Fedora, Gentoo,
openSUSE, Slackware (and linuxpackages.net), Source Mage, Ubuntu,
FreeBSD, NetBSD, OpenBSD, Fink and MacPorts. whohas is written in Perl
and was designed to help package maintainers find ebuilds, pkgbuilds
and similar package definitions from other distributions to learn
from. However, it can also be used by normal users who want to know:
 - Which distribution provides packages on which the user depends.
 - What version of a given package is in use in each distribution, or
   in each release of a distribution (implemented only for Debian).

%description -l hu.UTF-8
whohas egy parancssoros eszköz, amellyel különböző csomaglistákat
kérhetsz le - jelenleg Arch, Debian, Fedora, Gentoo, openSUSE,
Slackware (és a linuxpackages.net), Source Mage, Ubuntu, FreeBSD,
NetBSD, OpenBSD, Fink és MacPorts támogatott. whohas Perl-ben íródott
és a csomagkarbantartóknak segít ebuild-ek, pkgbuild-ek és hasonló
csomagdefiníciók keresésében, hogy tanulhasson más disztribúciókból.
Azonban egyszerű felhasználó is használhatja, aki tudni akarja, hogy
 - Melyik disztribúció szállítja a keresett csomagot
 - Az adott csomag mely verzióit használják az egyes disztribúciókban,
   vagy a az adott disztribúció melyik kiadásában (csak Debian-ra).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
for dir in %{_bindir} %{_mandir}/man1 %{_mandir}/de/man1; do
	install -d $RPM_BUILD_ROOT${dir}
done
install program/whohas $RPM_BUILD_ROOT%{_bindir}
install usr/share/man/man1/whohas.1 $RPM_BUILD_ROOT%{_mandir}/man1
install usr/share/man/de/man1/whohas.1 $RPM_BUILD_ROOT%{_mandir}/de/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/whohas
%{_mandir}/man1/whohas*
%lang(de) %{_mandir}/de/man1/whohas*
%doc Changelog intro.html intro.txt html_assets
