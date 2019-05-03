import sys
from pathlib import Path
PROJECT_PATH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_PATH))

import pypandoc as pandoc
import app

# for content in app.config['contents'].values():
#     app.build(content)

notes = app.get_all_context_pages()
# fpath = 'test.md'
# output = pandoc.convert_file(fpath, 'html', format='markdown+yaml_metadata_block')
