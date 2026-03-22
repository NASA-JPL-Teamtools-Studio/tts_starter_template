import pypandoc
from pathlib import Path
import os

def build_resume():
    # Setup paths relative to the project root
    project_root = Path(__file__).parent.parent.parent
    docs_dir = project_root / "docs"
    output_dir = project_root / "dist"
    output_dir.mkdir(exist_ok=True)

    resume_css = """
    @page { size: letter; margin: 0.5in 0.6in; }
    body { font-family: Helvetica, Arial, sans-serif; line-height: 1.25; font-size: 10pt; color: #1a1a1a; }
    h2 { border-bottom: 2px solid #2d4a77; text-transform: uppercase; margin-top: 12pt; margin-bottom: 6pt; font-size: 12pt; color: #2d4a77; font-weight: bold; }

    /* Styles for the job title lines */
    p { margin-top: 4pt; margin-bottom: 2pt; }
    p strong { font-size: 10.5pt; color: #000; }

    /* Tighter bullet lists */
    ul { margin-top: 2pt; margin-bottom: 6pt; padding-left: 1.2rem; }
    li { margin-bottom: 1pt; } 
    """

    temp_css = docs_dir / "style.css"
    temp_css.write_text(resume_css)

    try:
        md_path = docs_dir / "resume.md"
        pdf_path = output_dir / "Matt_Muszynski_Resume.pdf"
        
        if md_path.exists():
            print(f"Compiling {md_path.name} to {pdf_path.name}...")
            pypandoc.convert_file(
                str(md_path),
                'pdf',
                outputfile=str(pdf_path),
                extra_args=[
                    '--pdf-engine=weasyprint',
                    f'--css={temp_css}'
                ]
            )
            print("Success! Check the /dist folder.")
    finally:
        if temp_css.exists():
            temp_css.unlink()

if __name__ == "__main__":
    build_resume()