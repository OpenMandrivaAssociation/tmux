Summary:	Terminal multiplexer
Name:		tmux
Version:	3.0a
Release:	1
License:	BSD 
Group:		Terminals
Url:		http://tmux.sourceforge.net/ 
Source0:	https://github.com/tmux/tmux/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(ncurses)

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup -q

%build
%configure
%make_build

%install
install -d %{buildroot}%{_bindir}
install -m 755 tmux %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 644 tmux.1 %{buildroot}%{_mandir}/man1

%files
%doc README CHANGES
%{_bindir}/tmux
%{_mandir}/man1/tmux.*
