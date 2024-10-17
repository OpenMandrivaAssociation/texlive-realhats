Name:		texlive-realhats
Version:	66924
Release:	1
Summary:	Put real hats on symbols instead of ^
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/realhats
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package makes \hat put real hats on symbols. The
package depends on amsmath, calc, graphicx, ifthen, lcg, and
stackengine.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/realhats
%{_texmfdistdir}/tex/latex/realhats
%doc %{_texmfdistdir}/doc/latex/realhats

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
