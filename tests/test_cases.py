import os
import sqlite3
import bcrypt
import pytest

from PharmacyLogs.patientLog import patientLog
from PharmacyLogs.pharmacistLog import pharmacistLog



@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    os.makedirs("PharmacyLogs", exist_ok=True)
    return tmp_path


def test_patientlog_insert_and_fetch(sandbox):
    plog = patientLog()
    plog.DB_PATH = "PharmacyLogs/patientLog.db"
    plog.create_table()

    plog.insert("Alice", "Smith", "2000-01-01", "pw123", "alice@example.com")

    with sqlite3.connect(plog.DB_PATH) as conn:
        row = conn.execute(
            "SELECT * FROM patientLog WHERE email = ?",
            ("alice@example.com",)
        ).fetchone()

    assert row is not None
    assert row[5] == "alice@example.com"

    stored = row[4]
    if isinstance(stored, str):
        stored = stored.encode()

    assert bcrypt.checkpw("pw123".encode(), stored)


def test_pharmacistlog_insert_and_fetch(sandbox):
    phlog = pharmacistLog()
    phlog.DB_PATH = "PharmacyLogs/pharmacistLog.db"
    phlog.create_table()

    phlog.insert(101, "Jane", "Doe", "jane@pharm.com", "pw456")

    with sqlite3.connect(phlog.DB_PATH) as conn:
        row = conn.execute(
            "SELECT * FROM pharmacistLog WHERE email = ?",
            ("jane@pharm.com",)
        ).fetchone()

    assert row is not None
    assert row[3] == "jane@pharm.com"

    stored = row[4]
    if isinstance(stored, str):
        stored = stored.encode()

    assert bcrypt.checkpw("pw456".encode(), stored)




"""
Expected output:

$ python -m pytest -q
2 passed in 0.xx s
"""