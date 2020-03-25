import multiprocessing as mp
import time
import pypandoc as pandoc
from pathlib import Path
from shutil import rmtree, copyfile
from . import BASE_CONFIG, PROJECT_PATH, TEMPLATE_PATH, DOC_EXTENSIONS, CONTEXTS, log


def md_to_html(filepath, output_filepath):
    """
    Use Pandoc to convert Markdown file to HTML.

    Args:
        filepath (str): Markdown file path relative to `PROJECT_PATH`
        outputpath_filepath (str): Output HTML file path relative to `PROJECT_PATH`

    Returns:
        outputpath_filepath (pathlib.Path): Output HTML file path relative to `PROJECT_PATH`
    """
    filepath = PROJECT_PATH / Path(filepath)
    output_filepath = PROJECT_PATH / Path(output_filepath)
    pandoc.convert_file(
        filepath,
        "html+fenced_divs+definition_lists+link_attributes",
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
    print(context)
    source_path = context.source_path

    url = context.root_url
    if url[0] == "/":
        url = url[1:]
    output_path = TEMPLATE_PATH / Path(url)
    log.info(f"Building context files to: {output_path}")

    # Backup the build directory in templates
    backup = Path(TEMPLATE_PATH / f"{output_path.name}.bak")
    if output_path.exists():
        log.debug(f"{output_path.name} -> {backup.name}")
        output_path.rename(backup)

    output_path.mkdir()
    try:
        # Convert Markdown, HTML notes to HTML
        # notes = []
        # for note in sorted(source_path.glob(f"**/*")):
        #     if not note.is_file():
        #         continue
        #     if hasattr(context, "ignore_path"):
        #         if str(note.relative_to(source_path)) in context.ignore_path:
        #             continue
        #         if set(note.relative_to(source_path).parents) & set(
        #             Path(p) for p in context.ignore_path
        #         ):
        #             continue
        #     notes.append(note)

        def subproccess_md_to_html(note):
            # Add parent directory
            note = Path(note)
            note = note.relative_to(
                list(note.parents)[-2]
            )  # e.g., notebook, notebook/note.md
            Path.mkdir(output_path / note, parents=True, exist_ok=True)

            # Determine output filename
            if note.suffix[1:] in DOC_EXTENSIONS:
                outputfile = output_path / (note.stem + ".html")
            else:
                outputfile = output_path / note

            # Write to file
            log.debug(f"{note} > {outputfile}")
            print(note, outputfile)
            if note.suffix == ".md":
                outputfile = md_to_html(note.absolute(), outputfile)
            else:
                print(context.source_path / note, str(outputfile))
                copyfile(context.source_path / note, str(outputfile))

            # Check output file was created.
            if not outputfile.exists():
                raise FileNotFoundError(
                    "Output file(s) were deleted in middle of process. Please clean and restart the build."
                )

        processes = []
        for note in context.source_files:
            p = mp.Process(target=subproccess_md_to_html, args=(note,))
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
