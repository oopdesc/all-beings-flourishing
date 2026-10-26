"""Local structural checks for the book. No network or external packages."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def validate():
    references = load('research/REFERENCES.json')
    claims = load('research/CLAIMS.json')
    ids = {x['id'] for x in references}
    numbers = {x['number'] for x in references}
    assert len(ids) == len(references), 'Duplicate reference IDs'
    assert numbers == set(range(1, len(references) + 1)), 'Reference numbering gap'
    assert len({x['id'] for x in claims}) == len(claims), 'Duplicate claim IDs'
    allowed = {'empirical', 'normative', 'conditional', 'unresolved'}
    for claim in claims:
        assert set(claim['sources']) <= ids, claim['id']
        assert set(claim['basis_types']) <= allowed, claim['id']
        assert claim['limit'] and claim['update_condition'], claim['id']
    chapters = sorted((ROOT/'manuscript').glob('*.md'))
    assert len(chapters) == 32, 'Expected introduction, 24 chapters, appendices, bibliography and colophon'
    cited = set()
    for chapter in chapters:
        assert not chapter.is_symlink(), 'Manuscripts must be regular local files'
        text = chapter.read_text(encoding='utf-8')
        if not chapter.name.startswith('30_'):
            cited.update(map(int, re.findall(r'\[(\d+)\]', text)))
        assert '\ufffd' not in text, 'Replacement character found'
    assert cited <= numbers, 'Citation points to a missing source'
    assert 'CC BY-SA 4.0' in (ROOT/'LICENSE.md').read_text(encoding='utf-8')
    print(f'OK: {len(chapters)} manuscript sections, {len(references)} references, {len(claims)} claims')
    print('Structural checks do not certify truth, completeness, privacy or ethical validity.')

if __name__ == '__main__':
    try:
        validate()
    except (AssertionError, KeyError, ValueError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
