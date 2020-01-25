Summary:	whohas is a command line tool that allows querying several package lists at once
Summary(hu.UTF-8):	whohas egy parancssoros eszköz, amellyel különböző csomaglistákat kérhetsz le egyszerre
Summary(pl.UTF-8):	Konsolowe narzędzie pozwalacjące przeszukiwać kilka list pakietów jednocześnie
Name:		whohas
Version:	0.29
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.philippwesche.org/200811/whohas/%{name}-%{version}.tar.gz
# Source0-md5:	d12590e7d2c3c123b4cfb5b93ed4e902
URL:		http://www.philippwesche.org/200811/whohas/intro.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
whohas is a command line tool that allows querying several package
lists at once - currently supported are Arch, Debian, Fedora, Gentoo,
openSUSE, Slackware (and linuxpackages.net), Source Mage, Ubuntu,
FreeBSD, NetBSD, OpenBSD, Fink and MacPorts. whohas is written in Perl
and was designed to help package maintainers find ebuilds, pkgbuilds
and similar package definitions from other distributions to learn
from.

However, it can also be used by normal users who want to know:
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

%description -l pl.UTF-8
whohas jest konsolowym narzędziem, które pozwala przeszukiwać
jednocześnie wiele list pakietów. Aktualnie obsługiwane dystrybucje
to: Arch, Debian, Fedora, Gentoo, openSUSE, Slackware (and
linuxpackages.net), Source Mage, Ubuntu, FreeBSD, NetBSD, OpenBSD,
Fink and MacPorts. whohas jest napisany w Perlu. Głównym celem
projektu jest stworzenie narzędzia dla opiekunów pakietów,
pozwalającego im na łatwe znajdowanie ebuildów, pkgbuildów i innych
definicji pakietów w innych dystrybucjach, na podstawie których mogą
pracować nad pakietwami w swoich dystrybucjach. Jednak whohas może być
również przydatne dla zwykłych uzytkowników, którzy chcieliby się
dowiedzieć:
 - która dystrybucja dostarcza potrzebne im pakiety,
 - jaka wersja danego pakietu jest dostępna w której dystrybucji, lub
   wydaniu dystrybucji (funkcja zaimplementowana jedynie dla Debiana).

%prep
%setup -q
mv program/* .
mv usr/share/man .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_mandir}/de/man1}
install -p whohas $RPM_BUILD_ROOT%{_bindir}
cp -a man/man1/whohas.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a man/de/man1/whohas.1 $RPM_BUILD_ROOT%{_mandir}/de/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog intro.html intro.txt html_assets
%attr(755,root,root) %{_bindir}/whohas
%{_mandir}/man1/whohas.1*
%lang(de) %{_mandir}/de/man1/whohas.1*
