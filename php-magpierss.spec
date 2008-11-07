Summary:	MagpieRSS is an RSS parser written in PHP
Name:		php-magpierss
Version:	0.72
Release:	1
License:	GPL v2+
Group:		Development/Languages/PHP
URL:		http://magpierss.sourceforge.net/
Source0:	http://dl.sourceforge.net/magpierss/magpierss-%{version}.tar.gz
# Source0-md5:	04baa80bd07b078dd6ddd789ac659809
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MagpieRSS is a set of php files designed to parse RSS XML for usage in
PHP code. MagpieRSS is compatible with RSS 0.9 through RSS 1.0.

%prep
%setup -q -n magpierss-%{version}
chmod 644 scripts/*.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir}/magpierss,%{_examplesdir}/%{name}-%{version}}
cp -a rss_cache.inc $RPM_BUILD_ROOT%{php_data_dir}/magpierss
cp -a rss_fetch.inc $RPM_BUILD_ROOT%{php_data_dir}/magpierss
cp -a rss_parse.inc $RPM_BUILD_ROOT%{php_data_dir}/magpierss
cp -a rss_utils.inc $RPM_BUILD_ROOT%{php_data_dir}/magpierss
cp -a extlib $RPM_BUILD_ROOT%{php_data_dir}/magpierss
cp -a scripts/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES INSTALL NEWS README TROUBLESHOOTING cookbook htdocs
%{php_data_dir}/magpierss
%{_examplesdir}/%{name}-%{version}
