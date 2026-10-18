import sys, json, subprocess, time, glob
out = {}
for p in sorted(glob.glob('opcion-*/**/*.html', recursive=True)):
    r = subprocess.run(['curl', '-s', '-H', 'Content-Type: text/html; charset=utf-8', '-A', 'amari-audit', '--data-binary', '@' + p, 'https://validator.w3.org/nu/?out=json'], capture_output=True, text=True).stdout
    m = json.loads(r, strict=False)['messages']
    e = [x for x in m if x['type'] == 'error']
    w = [x for x in m if x.get('subType') == 'warning']
    out[p] = {'errors': len(e), 'warnings': len(w), 'detail': sorted(set(f"{x.get('lastLine')}: {x['message'][:90]}" for x in e))[:8], 'warn': sorted(set(x['message'][:70] for x in w))}
    print(p, len(e), 'errores', len(w), 'avisos', out[p]['detail'] or '', out[p]['warn'] or '')
    time.sleep(1)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
