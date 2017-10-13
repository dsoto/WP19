filters = --filter pandoc-crossref \
		  --filter pandoc-citeproc \
          --csl elsevier-with-titles.csl \
		  --bibliography bibliography.yaml

all: out/wp19_outline.pdf \
	 out/wp19_outline.docx \
	 out/wp19_outline.html \
	 out/wp19_outline.tex \
	 # out/wp19_output_outline.md

# TODO: link output tables and figures and notebooks in dependencies
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --print-to-pdf http://danielrsoto.com/200/syllabus.html


# $@ is the target variable (left side of colon)
# $< is the first prerequisite (right side of colon)

out/tmp_output.md: outline.md
	python include_tables.py outline.md $@

out/wp19_outline.pdf: out/tmp_output.md
	pandoc $(filters) \
	       -o $@ $<

out/wp19_outline.docx: out/tmp_output.md
	pandoc $(filters) \
	       -o $@ $<

out/wp19_outline.html: out/tmp_output.md
	pandoc $(filters) \
		   -c github-pandoc.css \
	       -o $@ $<

out/wp19_outline.tex: out/tmp_output.md
	pandoc $(filters) \
		   -s \
	       -o $@ $<
