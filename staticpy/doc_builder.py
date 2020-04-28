import multiprocessing as mp
import time
import pypandoc as pandoc
from pathlib import Path
from shutil import rmtree, copyfile
from . import (
    BASE_CONFIG,
    PROJECT_PATH,
    TEMPLATE_PATH,
    PANDOC_EXTENSIONS,
    DOC_EXTENSIONS,
    CONTEXTS,
    log,
)


def md_to_html(filepath, output_filepath):
    """
    Use Pandoc to convert Markdown file to HTML.

    Args:
        filepath (str): File path to markdown file
        outputpath_filepath (str): File path to output HTML file

    Returns:
        outputpath_filepath (pathlib.Path): Output HTML file path relative to `PROJECT_PATH`
    """
    pandoc.convert_file(
        str(filepath),
        PANDOC_EXTENSIONS,
        # "html+definition_lists+link_attributes",
        outputfile=str(output_filepath),
        extra_args=["--mathjax"],
    )
    return output_filepath


def build(context):
    """
    Builds all files in the context's source path and output it to `TEMPLATES_PATH` with its named specified by the context's URL.

    * Markdown files are converted to HTML with Pandoc.
    * Other files are directly copied to the output.
    """
    # Get path of source input folder
    source_path = Path(context.source_path)

    # Get path of output folder
    output_path = TEMPLATE_PATH / source_path.stem
    log.info(f"Building context files to {output_path}")

    # Backup the output folder
    backup = output_path.with_suffix(".bak")
    if output_path.exists():
        log.info(f"{output_path.name} -> {backup.name}")
        output_path.rename(backup)

    output_path.mkdir()

    def subproccess_md_to_html(source_file):
        """
        Args:
            source_file (str): File path to the source file relative to `PROJECT_PATH`.
        """
        source_file = Path(source_file)
        log.info(f"Processing source file {source_file}")

        # Make parent folders
        parent = source_file.parent
        log.info(f"mkdir {TEMPLATE_PATH / parent}")
        Path.mkdir(TEMPLATE_PATH / parent, parents=True, exist_ok=True)

        # Determine output filename
        if source_file.suffix[1:] in DOC_EXTENSIONS:
            outputfile = TEMPLATE_PATH / source_file.with_suffix(".html")
        else:
            outputfile = TEMPLATE_PATH / source_file

        # Write to file
        log.info(f"{PROJECT_PATH / source_file} -> {outputfile}")
        if source_file.suffix == ".md":
            outputfile = md_to_html(PROJECT_PATH / source_file, outputfile)
        else:
            copyfile(PROJECT_PATH / source_file, outputfile)

        # Check output file was created.
        if not outputfile.exists():
            raise FileNotFoundError(
                "Output file(s) were deleted in middle of process. Please clean and restart the build."
            )

    try:
        processes = []
        for source_file in context.source_files:
            # source_file is relative to PROJECT_PATH
            p = mp.Process(target=subproccess_md_to_html, args=(source_file,))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        # Success, remove backup
        if backup.exists():
            rmtree(str(backup))

    except Exception as e:  # Recover backup when fails
        log.exception(e)
        rmtree(str(output_path))
        if backup.exists():
            backup.rename(output_path)


def build_all():
    """Run build on all context found in configuration."""
    start = time.time()

    for context in CONTEXTS.values():
        build(context)

    return time.time() - start
