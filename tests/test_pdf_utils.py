import pytest
import os

from utils import pdf_utils


def test_generate_pdf_bytes_skips_if_missing():
    # If fpdf isn't installed the helper returns None — ensure graceful behavior
    pdf_bytes = pdf_utils.generate_pdf_bytes("Test content")
    if pdf_bytes is None:
        pytest.skip("fpdf not installed; skipping PDF tests")
    assert isinstance(pdf_bytes, (bytes, bytearray))


def test_save_pdf(tmp_path):
    pdf_bytes = pdf_utils.generate_pdf_bytes("This is a test plan")
    if pdf_bytes is None:
        pytest.skip("fpdf not installed; skipping PDF tests")

    outdir = tmp_path / "out"
    saved = pdf_utils.save_pdf("This is a test plan", directory=str(outdir))
    assert saved is not None
    assert os.path.exists(saved)
