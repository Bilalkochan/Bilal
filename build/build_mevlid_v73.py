from pathlib import Path
import zipfile

src = Path('source.html').read_text(encoding='utf-8-sig')
patch = Path('build/mevlid-v73-patch.html').read_text(encoding='utf-8')

src = src.replace('905523935851', '905523925851')
src = src.replace('0552 393 58 51', '0552 392 58 51')
src = src.replace('05523935851', '05523925851')

assert '{#' not in patch, 'Twig comment opener detected in V73 patch'
out = src.rstrip() + '\n' + patch.lstrip() + '\n'

assert '905523935851' not in out, 'Old WhatsApp number remains'
assert '0552 393 58 51' not in out, 'Old display number remains'
assert 'hk-v73-final-fixes' in out
assert 'hk-v73-final-script' in out
assert '60,120,180,240' in out
assert '50,100,150,200' in out
assert 'HESAP BİLGİLERİNE GİT' in out
assert len(out) > len(src)

html = Path('mevlid-v73-toplu.html')
html.write_text(out, encoding='utf-8')

with zipfile.ZipFile('mevlid-v73-toplu.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(html, html.name)

print('SOURCE_BYTES', len(src.encode('utf-8')))
print('OUTPUT_BYTES', len(out.encode('utf-8')))
print('CORRECT_WA_COUNT', out.count('905523925851'))
print('ACCOUNT_POPUP_OK', 'HESAP BİLGİLERİNE GİT' in out)
print('SYRIA_PRESETS_OK', '60,120,180,240' in out)
print('AFGHAN_PRESETS_OK', '50,100,150,200' in out)
