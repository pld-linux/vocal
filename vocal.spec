# TODO:
#  - make it from sources!!
#  - make separate packages:
#	- webpages
#	- gua
#	- voicemail...
#  - move some human-friendly place...
Summary:	vocal
Summary(pl):	vocal
Name:		vocal
Version:	1.5.0
Release:	0.3
License:	BSD-like (? please check)
Group:		Libraries
Source0:	http://www.vovida.org/downloads/%{name}/%{version}/rh73/%{name}bin-%{version}-20.i386.rpm
URL:		http://www.vovida.org/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vocaldir	/usr/local/vocal

%description
The Vovida Open Communication Application Library (VOCAL) is an open
source project targeted at facilitating the adoption of VoIP in the
marketplace. VOCAL provides the development community with software
and tools needed to build new and exciting VoIP features, applications
and services. The software in VOCAL includes a SIP based Redirect
Server, Feature Server, Provisioning Server and Marshal Proxy. This is
the stable development branch of the VOCAL

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -i -d

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,vocal,sysconfig},%{_mandir}/man{1,5,8},%{vocaldir}/etc,%{_bindir},%{_sbindir}}

install usr/local/vocal/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install usr/local/vocal/man/man5/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install usr/local/vocal/man/man8/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install usr/local/vocal/bin/cdrserv $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/FileDataStoreWrapper $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/fs $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/ms $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/pserver $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/rs $RPM_BUILD_ROOT%{_sbindir}
install usr/local/vocal/bin/gua $RPM_BUILD_ROOT%{_bindir}

# remove trash first:
rm usr/local/vocal/bin/{vocalstart,cdrserv,FileDataStoreWrapper,fs,ms,pserver,rs,gua}
cp -rf usr/local/vocal/bin/* $RPM_BUILD_ROOT%{vocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/share/doc/%{name}bin-%{version}/* usr/local/vocal/bin/sample-ua-config
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{vocaldir}/Tone/*
%attr(755,root,root) %{vocaldir}/allinoneconfigure/allinoneconfigure
%attr(755,root,root) %{vocaldir}/allinoneconfigure/*.pl
%{vocaldir}/allinoneconfigure/*.dtd
%{vocaldir}/allinoneconfigure/*.xml
%{vocaldir}/allinoneconfigure/*.sed
%{vocaldir}/allinoneconfigure/*.conf
%{vocaldir}/voicemail/*
%{vocaldir}/webpages/*
%{vocaldir}/provisioning/xml/*.xml
%{vocaldir}/manageusers
%{vocaldir}/verifysip
%{vocaldir}/vocalctl
%{vocaldir}/vocald
%dir /etc/vocal
%dir %{vocaldir}
%dir %{vocaldir}/Tone
%dir %{vocaldir}/allinoneconfigure
%dir %{vocaldir}/etc
%dir %{vocaldir}/provisioning
%dir %{vocaldir}/provisioning/xml
%dir %{vocaldir}/voicemail
%dir %{vocaldir}/webpages
%{vocaldir}/*.cfg
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
