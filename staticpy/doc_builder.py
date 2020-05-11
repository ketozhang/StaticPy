"""Build sources files located in each context's source folder to each context's content folder"""
import os
import itertools
import multiprocessing as mp
import time
import pypandoc as pandoc
from pathlib import Path
from shutil import rmtree, copyfile
from timeit import default_timer as timer
from . import (
    BASE_CONFIG,
    PROJECT_PATH,
    TEMPLATE_PATH,
    PANDOC_EXTENSIONS,
    DOC_EXTENSIONS,
    CONTEXTS,
    log,
    Context,
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


def build(context: Context):
    """
    Builds all files in the context's source path and output the source files to a file of the same name in the context's content path.

    The build process the files with the following rules:
        * Markdown files are converted to HTML with Pandoc.
        * Other files are directly copied to the output.

    The following source files/folders are ignored:
        * Empty folders
        * Files and subfiles of folders specificed by the config (`BASE_CONFIG[<context>]["ignored_paths"]`).
    """
    # Get path of source input folder
    source_folder = Path(context.source_folder)

    # Get path of output content folder
    output_folder = Path(context.content_folder)
    log.info(f"Building context files to {output_folder}")

    # Backup the output content folder
    backup = output_folder.with_suffix(".bak")
    if output_folder.exists():
        log.info(f"{output_folder.name} -> {backup.name}")
        output_folder.rename(backup)

    output_folder.mkdir()

    try:
        # Convert source file to content file
        # Multiprocess with process pool
        n_cpu = int(os.environ.get("STATICPY_MAX_CPU_USE", mp.cpu_count()))
        with mp.Pool(processes=n_cpu) as pool:
            args = itertools.product([context], context.source_files)
            pool.starmap(convert_source_to_content, args)

        # Multiprocess with process object
        # processes = []
        # for source_file in context.source_files:
        #     # source_file is relative to PROJECT_PATH
        #     p = mp.Process(target=convert_source_to_content, args=(source_file,))
        #     processes.append(p)
        #     p.start()

        # for process in processes:
        #     process.join()

        # Success, remove backup
        if backup.exists():
            rmtree(str(backup))

    except Exception as e:  # Recover backup when fails
        log.exception(e)
        rmtree(str(output_folder))
        if backup.exists():
            backup.rename(output_folder)


def build_all():
    """Run build on all context found in configuration."""
    print("\n" + f"{' BUILDING ':=^80}")
    start = timer()

    for context in CONTEXTS.values():
        build(context)

    return timer() - start


def convert_source_to_content(context, source_file):
    source_file = Path(source_file)
    msg = f"Processing source file {source_file.relative_to(PROJECT_PATH)}"
    log.info("{:.<80}".format(msg))

    # Determine output content file path
    outputfile = Path(context.source_to_content(source_file))

    # Make parent folders of the output file
    parent = outputfile.parent
    log.info(f"mkdir {parent.relative_to(PROJECT_PATH)}")
    Path.mkdir(parent, parents=True, exist_ok=True)

    if source_file.suffix[1:] in DOC_EXTENSIONS:
        outputfile = outputfile.with_suffix(".html")

    # Write to file
    log.info(
        f"{source_file.relative_to(PROJECT_PATH)} -> {outputfile.relative_to(PROJECT_PATH)}"
    )
    if source_file.suffix == ".md":
        outputfile = md_to_html(source_file, outputfile)
    else:
        copyfile(source_file, outputfile)

    # Check output file was created.
    if not outputfile.exists():
        raise FileNotFoundError(
            "Output file(s) were deleted in middle of process. Please clean and restart the build."
        )
