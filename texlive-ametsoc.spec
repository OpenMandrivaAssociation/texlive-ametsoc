# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ametsoc
# catalog-date 2008-09-04 00:14:12 +0200
# catalog-license lppl
# catalog-version 3.0
Name:		texlive-ametsoc
Version:	3.0
Release:	1
Summary:	Official American Meteorological Society Latex Template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ametsoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ametsoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ametsoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package contains all the files necessary to write an
article using latex for the American Meteorological Society
journals. The article and bibliography style files are provided
along with two PDFs describing the use of the files and a blank
template for authors to use in writing their article. Also
available is a separate style file used to format a two-column,
journal page layout draft for the author's personal use.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ametsoc/ametsoc.bst
%{_texmfdistdir}/tex/latex/ametsoc/ametsoc.sty
%{_texmfdistdir}/tex/latex/ametsoc/ametsoc2col.sty
%doc %{_texmfdistdir}/doc/latex/ametsoc/AMS_References.pdf
%doc %{_texmfdistdir}/doc/latex/ametsoc/README
%doc %{_texmfdistdir}/doc/latex/ametsoc/amspaper.pdf
%doc %{_texmfdistdir}/doc/latex/ametsoc/amspaper.tex
%doc %{_texmfdistdir}/doc/latex/ametsoc/amspaper2col.pdf
%doc %{_texmfdistdir}/doc/latex/ametsoc/bibliography/database.bib
%doc %{_texmfdistdir}/doc/latex/ametsoc/bibliography/references.bib
%doc %{_texmfdistdir}/doc/latex/ametsoc/blank_template.pdf
%doc %{_texmfdistdir}/doc/latex/ametsoc/blank_template.tex
%doc %{_texmfdistdir}/doc/latex/ametsoc/figures/figure01.eps
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
