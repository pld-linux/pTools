Summary:	Process Information Utilities
Summary(pl):	Narzêdzie Informuj±ce o Procesach
Name:		pTools
Version:	0.1
Release:	8
License:	GPL
Group:		Applications/System
#Source0:	http://www.cs.fsu.edu/~oberther/pTools/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1b07f7ae2f3af3eb6ec12361e0a4d73c
Patch0:		%{name}-procps.patch
BuildRequires:	procps-devel >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pTools project is an attempt to duplicate the functionality of the
Sun Microsystems /usr/proc/bin/ toolset. Each of the tools will behave
in a similiar manner and return the same relevent information for the
inspected process.

%description -l pl
Projekt pTools jest prób± stworzenia duplikatu funkcjonalno¶ci zbioru
narzêdzi /usr/proc/bin firmy Sun Microsystems. Ka¿de z narzêdzi bêdzie
zachowywa³o siê w podobny sposób oraz zwraca³o t± sam± istotn±
informacjê na temat kontrolowanego procesu.

%prep
%setup -q
%patch0 -p1

%build
# not autoconf-generated
./configure

%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for i in src/*; do
	[ ! -d $i ] && continue
	j=$(basename $i)
	p="$i/$j"
	[ ! -f "$p" ] && continue
	cp $p $RPM_BUILD_ROOT%{_bindir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO *.diff
%attr(755,root,root) %{_bindir}/*
