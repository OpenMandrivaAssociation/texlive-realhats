%global tl_name realhats
%global tl_revision 66924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.1
Release:	%{tl_revision}.1
Summary:	Put real hats on symbols instead of ^
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/realhats
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realhats.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package makes \hat put real hats on symbols. The package
depends on amsmath, calc, graphicx, ifthen, lcg, and stackengine.

