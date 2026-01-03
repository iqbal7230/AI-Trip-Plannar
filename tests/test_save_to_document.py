import tempfile
import os

from utils.save_to_document import save_document


def test_save_document_creates_file_and_returns_path(tmp_path):
    content = "This is a test plan."
    outdir = tmp_path / "output_dir"
    outdir_str = str(outdir)

    saved = save_document(content, directory=outdir_str)

    assert saved is not None
    assert os.path.exists(saved)
    with open(saved, 'r', encoding='utf-8') as f:
        text = f.read()
    assert "This is a test plan." in text
