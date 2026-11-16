import csv, json, re, sys
src, html_path = sys.argv[1], sys.argv[2]
mfn, ad, multi = {}, {}, {}
for r in csv.DictReader(open(src, encoding='utf-8')):
    h = r['hs6'].replace('.', '')
    if r['origin'] == 'ALL (MFN)':
        if int(r['cn_codes'] or 1) > 1: multi[h] = int(r['cn_codes'])
        lo, hi = r['duty_min'].strip(), r['duty_max'].strip()
        simple = lambda s: re.fullmatch(r'(\d+(?:\.\d+)?) %', s)
        if simple(lo) and simple(hi):
            a, b = float(simple(lo).group(1)), float(simple(hi).group(1))
            mfn[h] = a if a == b else [a, b]
        else:
            mfn[h] = lo if lo == hi else lo + ' to ' + hi
    elif r['anti_dumping_possible'] == 'yes':
        ad.setdefault(h, []).append(r['origin'])
data = json.dumps({'d': mfn, 'ad': {k: ','.join(v) for k, v in ad.items()}, 'm': multi}, separators=(',', ':'), ensure_ascii=True)
html = open(html_path, encoding='utf-8').read()
new, n = re.subn(r'/\*DUTY_START\*/.*?/\*DUTY_END\*/', lambda m: '/*DUTY_START*/' + data + '/*DUTY_END*/', html, flags=re.S)
assert n == 1, n
open(html_path, 'w', encoding='utf-8').write(new)
print(len(mfn), 'headings,', len(ad), 'with anti-dumping flags,', len(data), 'bytes')
