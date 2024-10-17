Name:		texlive-xelatex-dev
Version:	62145
Release:	2
Summary:	
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xelatex-dev
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xelatex-dev.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
