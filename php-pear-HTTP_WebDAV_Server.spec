%define		_class		HTTP
%define		_subclass	WebDAV
%define		upstream_name	%{_class}_%{_subclass}_Server

Name:		php-pear-%{upstream_name}
Version:	0.99.1
Release:	18
Summary:	WebDAV Server Baseclass
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRequires:	php-pear

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-14mdv2011.0
+ Revision: 667514
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-13mdv2011.0
+ Revision: 607112
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.99.1-12mdv2010.1
+ Revision: 477902
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.99.1-11mdv2010.0
+ Revision: 426648
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-10mdv2009.1
+ Revision: 321870
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.99.1-9mdv2009.0
+ Revision: 224749
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-8mdv2008.1
+ Revision: 178519
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-7mdv2007.0
+ Revision: 81885
- Import php-pear-HTTP_WebDAV_Server

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-1mdk
- initial Mandriva package (PLD import)

