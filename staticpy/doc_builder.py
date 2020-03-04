import multiprocessing as mp
import time
import pypandoc as pandoc
from pathlib import Path
from shutil import rmtree, copyfile
from . import BASE_CONFIG, PROJECT_PATH, TEMPLATE_PATH, DOC_EXTENSIONS, log
from .source_handler import get_fpath


def md_to_html(file_or_path, outputfile):
    fpath = get_fpath(file_or_path)
    outputfile = get_fpath(outputfile)
    pandoc.convert_file(
        str(fpath),
        "html+fenced_divs+definition_lists+link_attributes",
        outputfile=str(outputfile),
        extra_args=["--mathjax"],
    )
    return outputfile


def build(context):
    """Converts the source directory (`source_path`) to a directory of html
    (`output_path`) outputted to the templates directory."""
    source_path = PROJECT_PATH / context["source_path"]

    url = context["source_path"]
    if url[0] == "/":
        url = url[1:]
    output_path = TEMPLATE_PATH / Path(url)
    log.info(f"Building context at: {url}")

    # Backup the build directory in templates
    backup = Path(TEMPLATE_PATH / f"{output_path.name}.bak")
    if output_path.exists():
        log.debug(f"{output_path.name} -> {backup.name}")
        output_path.rename(backup)

    output_path.mkdir()
    try:
        # Convert Markdown, HTML notes to HTML
        notes = [note for note in sorted(source_path.glob(f"**/*")) if note.is_file()]

        processes = []
        for note in notes:
            parent = note.relative_to(source_path).parent  # /path/to/note/

            def subprocess(note):
                # Add parent directory
                if note.parent.exists():
                    Path.mkdir(output_path / parent, parents=True, exist_ok=True)

                # Determine output filename
                if note.suffix[1:] in DOC_EXTENSIONS:
                    outputfile = output_path / parent / (note.stem + ".html")
                else:
                    outputfile = output_path / parent / note.name

                # Write to file
                log.debug(f"{note} > {outputfile}")
                if note.suffix == ".md":
                    outputfile = md_to_html(note.absolute(), outputfile)
                else:
                    copyfile(str(note), str(outputfile))

                # Check output file was created.
                if not outputfile.exists():
                    raise FileNotFoundError(
                        "Output file(s) were deleted in middle of process. Please clean and restart the build."
                    )

            p = mp.Process(target=subprocess, args=(note,))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        # Success, remove backup
        if backup.exists():
            rmtree(str(backup))
    except Exception as e:  # Recover backup when fails
        log.error(e)
        rmtree(str(output_path))
        if backup.exists():
            backup.rename(output_path)


def build_all():
    """Run build on all context found in configuration."""
    start = time.time()

    for context in BASE_CONFIG["contexts"].values():
        build(context)

    return time.time() - start
