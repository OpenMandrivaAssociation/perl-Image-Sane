%define upstream_name Image-Sane
%define upstream_version 0.14

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        2
Summary:        Perl extension for the SANE (Scanner Access Now Easy) Project
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            https://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/authors/id/R/RA/RATCLIFFE/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  pkgconfig(sane-backends) >= 1.0.19
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)

%description
These Perl bindings for the SANE (Scanner Access Now Easy) Project allow
you to access SANE-compatible scanners in a Perlish and object-oriented
way, freeing you from the casting and memory management in C, yet remaining
very close in spirit to original API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod -x examples/*

%build
%__perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
%make_build

%install
%make_install

find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Image*
%{_mandir}/man3/*
