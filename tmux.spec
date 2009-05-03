%define name	tmux
%define version	0.8
%define release	%mkrel 1

Summary:	Terminal multiplexer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	BSD 
Group:		Terminals
Url:		http://tmux.sourceforge.net/ 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ncurses-devel

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup -q

%build
CFLAGS="-I/usr/include/asm" %make

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}%{_bindir}
%__install -m 755 tmux %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 tmux.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ NOTES TODO CHANGES examples/
%_bindir/tmux
%_mandir/man1/tmux.*

