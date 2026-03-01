"""Enhanced Flet CodeEditor with file open/save/save-as/close capabilities."""

from fce_enhanced.editor import EnhancedCodeEditor, main, run
from fce_enhanced.file_dialog import open_file, save_file
from fce_enhanced.languages import EXTENSION_TO_LANGUAGE, language_for_path
from fce_enhanced.search import SearchReplaceBar

__all__ = [
    "EnhancedCodeEditor",
    "EXTENSION_TO_LANGUAGE",
    "SearchReplaceBar",
    "language_for_path",
    "main",
    "open_file",
    "run",
    "save_file",
]
