
%define realname   Text-Tabs+Wrap
%define version    2009.0305
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Wraps lines to make simple paragraphs
Source:     http://www.cpan.org/modules/by-module/Text/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
Text::Tabs does about what the unix utilities expand(1) and unexpand(1) do.
Given a line with tabs in it, expand will replace the tabs with the
appropriate number of spaces. Given a line with or without tabs in it,
unexpand will add tabs when it can save bytes by doing so (just like
'unexpand -a'). Invisible compression with plain ASCII!





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGELOG README
%{_mandir}/man3/*
%perl_vendorlib/*


