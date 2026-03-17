import re
import sys
from pathlib import Path
from typing import List, NamedTuple, Optional, Tuple

DIRS_TO_CHECK = ["pm", "stadgar", "other_documents"]
WARNING_WORDS = []
ABBREVIATIONS = re.compile(r"\b(?:t\.ex|t\.o\.m|fr\.o\.m|d\.v\.s|m\.m|e\.g|i\.e|etc)\.", re.IGNORECASE)

#The starting section of Memos that should always have the following sections
SWE_FORMALIA = "Formalia"
ENG_FORMALIA = "Formalities"
SWE_FORMALIA_PARTS = ["Syfte", "Historik", "Ändrande av PM"]
ENG_FORMALIA_PARTS = ["Purpose", "History", "Revising this Memo"]

SWE_CHANGE = "Senast ändrat:"
ENG_CHANGE = "Last revision:"

class ValidationError(NamedTuple):
	"""Represents a single validation error."""
	file_path: Path
	message: str
	line_number: Optional[int] = None

	def __str__(self) -> str:
		"""Formats the error message for printing."""
		location = f"{self.file_path}:{self.line_number}" if self.line_number else str(self.file_path)
		return f"{location}: {self.message}"

def check_periods(lines: List[str], file_path: Path) -> List[ValidationError]:
	"""
	Checks for lines with more than one period. Enforcing that each line is a single sentence.

	It ignores periods used in URLs, abbreviations, and code blocks.
	"""
	errors: List[ValidationError] = []
	for i, line in enumerate(lines):
		text = line.strip()
		if (
			not text
			or text.startswith("#")
			or text.endswith(":")
			or ("stadgar.md" in file_path.name and text.startswith("|"))
		):
			continue

		text = re.sub(r"https?://\S+", "", text)  #Remove URLs
		text = re.sub(r"\]\([^\)]+\)", "]", text)  #Remove Markdown links
		text = re.sub(r"§\d+(?:\.\d+)*", "", text)  #Remove §1.2.3 section symbols
		text = re.sub(r"\.(?=\d)", "", text)  #Remove dots in numbers
		text = re.sub(r"^\d+\.", "", text)  #Remove list markers
		text = ABBREVIATIONS.sub("", text)  #Remove abbreviations

		if text.count(".") > 1:
			errors.append(ValidationError(file_path, f"Line has {text.count('.')} periods, expected max 1.", i + 1))
	return errors

def check_warning_words(lines: List[str], file_path: Path) -> List[ValidationError]:
	"""Checks for WARNING_WORDS that shouldn't be in the text."""
	errors: List[ValidationError] = []
	for i, line in enumerate(lines):
		for word in WARNING_WORDS:
			if re.search(r"\b" + re.escape(word) + r"\b", line, re.IGNORECASE):
				errors.append(ValidationError(file_path, f"Found warning word: '{word}'", i + 1))
	return errors

def check_file_boundaries(content: str, file_path: Path) -> List[ValidationError]:
	"""
	Checks for missing trailing newline and checks that the file does not start with a newline.
	"""
	errors: List[ValidationError] = []
	if content.startswith('\n') or content.startswith('\r\n'):
		errors.append(ValidationError(file_path, "File starts with an empty line.", line_number=1))

	if not content.endswith('\n'):
		errors.append(ValidationError(file_path, "File is missing a trailing newline."))
	elif content.endswith('\n\n') or content.endswith('\r\n\r\n'):
		errors.append(ValidationError(file_path, "File has multiple trailing newlines."))
	return errors

def check_pm_structure(content: str, file_path: Path, lang: str) -> List[ValidationError]:
	"""Validates Memo structure with required sections."""
	errors: List[ValidationError] = []

	if lang == "swe":
		h1_check = SWE_FORMALIA
		h2_checks = SWE_FORMALIA_PARTS
	else:
		h1_check = ENG_FORMALIA
		h2_checks = ENG_FORMALIA_PARTS

	if not re.search(r"^## \d+\.? " + re.escape(h1_check), content, re.MULTILINE):
		errors.append(ValidationError(file_path, f"Missing '## X {h1_check}' section."))

	missing_h2s = [h2 for h2 in h2_checks if not re.search(r"^### \d+\.\d+\.? " + re.escape(h2), content, re.MULTILINE)]
	if missing_h2s:
		errors.append(ValidationError(file_path, f"Missing '### X.Y' subsections: {', '.join(missing_h2s)}"))

	return errors

def check_weird_quotes(lines: List[str], file_path: Path) -> List[ValidationError]:
    """
    Checks for non-standard quote characters.
    """
    errors: List[ValidationError] = []
    for i, line in enumerate(lines):
        found = re.compile(r'[“”„‟«»‘’‚‛′″]').findall(line)
        if found:
            chars = ', '.join(sorted(set(found)))
            errors.append(ValidationError(file_path, f"Line has non-standard quote character: {chars}", i + 1))
    return errors

def extract_date(lines: List[str], prefix: str) -> Optional[Tuple[int, str]]:
	"""Extracts YYYY-MM-DD date from a line starting with the given prefix."""
	for i, line in enumerate(lines):
		if line.strip().startswith(prefix):
			match = re.search(r"(\d{4}-\d{2}-\d{2})", line)
			if match:
				return i + 1, match.group(1)
	return None

def extract_headers(lines: List[str]) -> List[Tuple[int, str]]:
	"""Extracts all Markdown headers."""
	return [(i + 1, line.strip()) for i, line in enumerate(lines) if line.strip().startswith("#")]

def compare_files(swe_path: Path, swe_lines: List[str], eng_path: Path, eng_lines: List[str]) -> List[ValidationError]:
	"""
	Compares Swedish and English file versions for consistency.

	- Line counts
	- Header numbering
	- Revision dates
	"""
	errors: List[ValidationError] = []

	if len(swe_lines) != len(eng_lines):
		errors.append(ValidationError(swe_path, f"Line count mismatch with {eng_path.name}: {len(swe_lines)} vs {len(eng_lines)}"))
		return errors

	swe_headers = extract_headers(swe_lines)
	eng_headers = extract_headers(eng_lines)
	if len(swe_headers) != len(eng_headers):
		errors.append(ValidationError(swe_path, f"Header count mismatch with {eng_path.name}: {len(swe_headers)} vs {len(eng_headers)}"))
	else:
		for (swe_line, swe_header), (eng_line, eng_header) in zip(swe_headers, eng_headers):
			if swe_line != eng_line:
				errors.append(ValidationError(swe_path, f"Header line number mismatch for '{swe_header}'. SWE line:{swe_line} vs ENG line:{eng_line}", swe_line))
				
			swe_match = re.match(r"^(#+ [\d\.]+)", swe_header)
			eng_match = re.match(r"^(#+ [\d\.]+)", eng_header)
			if swe_match and eng_match and swe_match.group(1).strip(".") != eng_match.group(1).strip("."):
				errors.append(ValidationError(swe_path, f"Header number mismatch: '{swe_header}' vs '{eng_header}' (ENG line {eng_line})", swe_line))

	swe_date_info = extract_date(swe_lines, SWE_CHANGE)
	eng_date_info = extract_date(eng_lines, ENG_CHANGE)
	if swe_date_info and eng_date_info:
		swe_line, swe_date = swe_date_info
		eng_line, eng_date = eng_date_info
		if swe_date != eng_date:
			errors.append(ValidationError(swe_path, f"Date mismatch: SWE '{swe_date}' vs ENG '{eng_date}' (ENG line {eng_line})", swe_line))
	elif swe_date_info and not eng_date_info:
		swe_line, swe_date = swe_date_info
		errors.append(ValidationError(swe_path, f"Missing '{ENG_CHANGE}' in ENG file (found '{swe_date}' in SWE).", swe_line))
	return errors

def process_file(file_path: Path, dir_name: str) -> Tuple[List[str], List[ValidationError]]:
	try:
		content = file_path.read_text(encoding="utf-8")
		lines = content.splitlines()
	except IOError as e:
		return [], [ValidationError(file_path, f"Could not read file: {e}")]

	errors: List[ValidationError] = []
	lang = file_path.parent.name

	errors.extend(check_periods(lines, file_path))
	errors.extend(check_warning_words(lines, file_path))
	errors.extend(check_file_boundaries(content, file_path))
	errors.extend(check_weird_quotes(lines, file_path))

	if dir_name == "pm":
		errors.extend(check_pm_structure(content, file_path, lang))

	return lines, errors

def main() -> int:
	all_errors: List[ValidationError] = []
	valid_files = 0
	invalid_files = 0
	base_path = Path(".")

	for dir_name in DIRS_TO_CHECK:
		swe_dir = base_path/dir_name/"swe"
		eng_dir = base_path/dir_name/"eng"

		if not swe_dir.is_dir():
			continue

		for swe_path in swe_dir.glob("*.md"):
			print(f"Checking {swe_path}...")
			file_errors: List[ValidationError] = []

			swe_lines, swe_errors = process_file(swe_path, dir_name)
			file_errors.extend(swe_errors)

			eng_path = eng_dir/swe_path.name
			if eng_path.exists():
				eng_lines, eng_errors = process_file(eng_path, dir_name)
				file_errors.extend(eng_errors)
				file_errors.extend(compare_files(swe_path, swe_lines, eng_path, eng_lines))
			else:
				file_errors.append(ValidationError(swe_path, f"Missing English version for {swe_path.name}"))

			if file_errors:
				invalid_files += 1
				all_errors.extend(file_errors)
			else:
				valid_files += 1

	print("" + "=" * 18)
	print("VALIDATION SUMMARY")
	print("=" * 18)

	if all_errors:
		all_errors.sort(key=lambda e: (str(e.file_path), e.line_number or 0))
		for err in all_errors:
			print(err)
	else:
		print("All checks passed!")

	print("=" * 18)
	print(f"Files Checked: {valid_files + invalid_files}")
	print(f"Valid Files:   {valid_files}")
	print(f"Invalid Files: {invalid_files}")
	print("=" * 18)

	return 1 if all_errors else 0

if __name__ == "__main__":
	sys.exit(main())
