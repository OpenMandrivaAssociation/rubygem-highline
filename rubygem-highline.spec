%define	oname	highline

Summary:	A high-level command-line IO library for ruby
Name:		rubygem-%{oname}
Version:	1.5.2
Release:	4
License:	GPLv2 or Ruby
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

for r in `find %{buildroot} -name \*.rb`; do
	sed -e 's#/usr/local/bin/ruby#/usr/bin/env ruby#g' -i $r
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-3mdv2011.0
+ Revision: 614772
- the mass rebuild of 2010.1 packages

* Thu Feb 04 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.2-2mdv2010.1
+ Revision: 500864
- drop invalid dependency on rubygem-ruby-hmac

* Thu Feb 04 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.2-1mdv2010.1
+ Revision: 500863
- import rubygem-highline


* Mon Feb  4 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.2-1
- initial release
