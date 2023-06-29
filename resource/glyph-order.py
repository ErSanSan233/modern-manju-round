import json

with open('modern-manju-reconfig-changeencodings-try-glyphs.json') as f:
    cs = json.load(f)

for glyph in cs:
    glyph['Encoding'][0] = glyph['Encoding'][0] + 8
    glyph['Encoding'][2] = glyph['Encoding'][0]
    if 'Refer' in glyph:
        glyph["Refer"][0] = glyph["Refer"][0] + 8

with open('res.json', 'w') as f:
    json.dump(cs, f)