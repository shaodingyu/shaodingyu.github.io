"""Include root-level teaching PDFs in MkDocs builds."""

from pathlib import Path

from mkdocs.structure.files import File


def on_files(files, config):
    """Expose the shared teaching_pdf directory to MkDocs link validation."""
    project_dir = Path(config.config_file_path).parent
    pdf_dir = project_dir / "teaching_pdf"

    for pdf_path in sorted(pdf_dir.rglob("*.pdf")):
        files.append(
            File(
                pdf_path.relative_to(project_dir).as_posix(),
                str(project_dir),
                config.site_dir,
                config.use_directory_urls,
            )
        )

    return files
