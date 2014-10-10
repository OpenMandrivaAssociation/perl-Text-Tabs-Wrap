%define realname   Text-Tabs+Wrap
%define upstream_version 2013.0523

Name:       perl-%{realname}
Version:    %perl_convert_version %{upstream_version}
Release:    2
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Wraps lines to make simple paragraphs
Source:     http://www.cpan.org/modules/by-module/Text/Text-Tabs+Wrap-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel


BuildArch: noarch

%description
Text::Tabs does about what the unix utilities expand(1) and unexpand(1) do.
Given a line with tabs in it, expand will replace the tabs with the
appropriate number of spaces. Given a line with or without tabs in it,
unexpand will add tabs when it can save bytes by doing so (just like
'unexpand -a'). Invisible compression with plain ASCII!



%prep
%setup -q -n %{realname}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGELOG README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2009.0305-3mdv2011.0
+ Revision: 658449
- rebuild for updates rpm-setup

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2009.0305-2mdv2010.0
+ Revision: 375889
- rebuild

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2009.0305-1mdv2010.0
+ Revision: 374455
- import perl-Text-Tabs+Wrap


* Mon May 11 2009 cpan2dist 2009.0305-1mdv
- initial mdv release, generated with cpan2dist



