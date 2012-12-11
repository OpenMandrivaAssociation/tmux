%define name	tmux
%define version	1.6
%define release 1

Summary:	Terminal multiplexer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	BSD 
Group:		Terminals
Url:		http://tmux.sourceforge.net/ 
BuildRequires:	ncurses-devel, libevent-devel

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup -q

%build
%configure2_5x
#./configure
%make

%install
%__install -d %{buildroot}%{_bindir}
%__install -m 755 tmux %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 tmux.1 %{buildroot}%{_mandir}/man1

%files
%doc FAQ NOTES TODO CHANGES examples/
%_bindir/tmux
%_mandir/man1/tmux.*



%changelog
* Thu Jan 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6-1
+ Revision: 769044
- version update 1.6

* Tue Jul 12 2011 Lev Givon <lev@mandriva.org> 1.5-1
+ Revision: 689730
- Update to 1.5.

* Wed Dec 29 2010 Lev Givon <lev@mandriva.org> 1.4-1mdv2011.0
+ Revision: 625751
- Update to 1.4.

* Wed Dec 22 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdv2011.0
+ Revision: 623880
- rebuilt against libevent 2.x

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 1.3-1mdv2011.0
+ Revision: 562837
- Update to 1.3.

* Thu Mar 11 2010 Lev Givon <lev@mandriva.org> 1.2-1mdv2011.0
+ Revision: 518231
- Update to 1.2.

* Sun Dec 06 2009 Lev Givon <lev@mandriva.org> 1.1-1mdv2010.1
+ Revision: 474239
- Update to 1.1.

* Mon Jul 27 2009 Lev Givon <lev@mandriva.org> 0.9-1mdv2010.0
+ Revision: 400827
- Update to 0.9.

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 0.8-1mdv2010.0
+ Revision: 371132
- Update to 0.8.

* Wed Feb 11 2009 Lev Givon <lev@mandriva.org> 0.7-1mdv2009.1
+ Revision: 339511
- Update to 0.7.

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 0.6-1mdv2009.1
+ Revision: 331825
- import tmux

