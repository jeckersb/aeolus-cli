%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname aeolus-image
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global mandir %{_mandir}/man1
%global rubyabi 1.8

Summary: Command-line interface for working with the Aeolus cloud suite
Name: rubygem-aeolus-image
Version: 0.1.0
Release: 3%{?dist}%{?extra_release}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://aeolusproject.org

# The source for this packages was pulled from the upstream's git repo.
# Use the following commands to generate the gem
# git clone  git://git.fedorahosted.org/aeolus/conductor.git
# git checkout next
# cd services/image_factory/aeolus-image
# rake gem
# grab image_factory_console-0.0.1.gem from the pkg subdir
Source0: %{gemname}-%{version}.gem

Requires: ruby(abi) = %{rubyabi}
Requires: rubygems
Requires: rubygem(nokogiri) >= 1.4.0
Requires: rubygem(rest-client)
Requires: rubygem(imagefactory-console) >= 0.4.0

BuildRequires: ruby
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
QMF Console for Aeolus Image Factory

%prep

%build

%install
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod 755
rmdir %{buildroot}%{gemdir}/bin

mkdir -p %{buildroot}%{mandir}
mv %{buildroot}%{geminstdir}/man/* %{buildroot}%{mandir}

%files
%defattr(-, root, root, -)
%{_bindir}/aeolus-image
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{mandir}/*

%changelog
* Wed Jul 20 2011 Mo Morsi <mmorsi@redhat.com>  - 0.0.1-3
- more updates to conform to fedora guidelines

* Fri Jul 15 2011 Mo Morsi <mmorsi@redhat.com>  - 0.0.1-2
- updated package to conform to fedora guidelines

* Mon Jul 04 2011  <mtaylor@redhat.com>  - 0.0.1-1
- Added man files

* Wed Jun 15 2011  <jguiditt@redhat.com> - 0.0.1-1
- Initial package