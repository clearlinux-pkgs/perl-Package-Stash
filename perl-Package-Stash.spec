#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-Stash
Version  : 0.38
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Package-Stash-0.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Package-Stash-0.38.tar.gz
Summary  : 'routines for manipulating stashes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Package-Stash-bin = %{version}-%{release}
Requires: perl-Package-Stash-license = %{version}-%{release}
Requires: perl-Package-Stash-man = %{version}-%{release}
Requires: perl-Package-Stash-perl = %{version}-%{release}
Requires: perl(Dist::CheckConflicts)
BuildRequires : buildreq-cpan
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Package-Stash,
version 0.38:
routines for manipulating stashes

%package bin
Summary: bin components for the perl-Package-Stash package.
Group: Binaries
Requires: perl-Package-Stash-license = %{version}-%{release}

%description bin
bin components for the perl-Package-Stash package.


%package dev
Summary: dev components for the perl-Package-Stash package.
Group: Development
Requires: perl-Package-Stash-bin = %{version}-%{release}
Provides: perl-Package-Stash-devel = %{version}-%{release}
Requires: perl-Package-Stash = %{version}-%{release}

%description dev
dev components for the perl-Package-Stash package.


%package license
Summary: license components for the perl-Package-Stash package.
Group: Default

%description license
license components for the perl-Package-Stash package.


%package man
Summary: man components for the perl-Package-Stash package.
Group: Default

%description man
man components for the perl-Package-Stash package.


%package perl
Summary: perl components for the perl-Package-Stash package.
Group: Default
Requires: perl-Package-Stash = %{version}-%{release}

%description perl
perl components for the perl-Package-Stash package.


%prep
%setup -q -n Package-Stash-0.38
cd %{_builddir}/Package-Stash-0.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-Stash
cp %{_builddir}/Package-Stash-0.38/LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-Stash/86fe74a925805c9016a91b52d3efab8705c51e94
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/package-stash-conflicts

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::Stash.3
/usr/share/man/man3/Package::Stash::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-Stash/86fe74a925805c9016a91b52d3efab8705c51e94

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/package-stash-conflicts.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Package/Stash.pm
/usr/lib/perl5/vendor_perl/5.30.3/Package/Stash/Conflicts.pm
/usr/lib/perl5/vendor_perl/5.30.3/Package/Stash/PP.pm
