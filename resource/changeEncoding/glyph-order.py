import json

with open("glyphs-encoding.json") as f:
    cs = json.load(f)

for glyph in cs:
    res_id = glyph['Encoding'][0]

    if res_id > 15:
        glyph['Encoding'][0] = res_id + 8
        glyph['Encoding'][2] = res_id + 8
        if 'Refer' in glyph:
            if glyph["Refer"][0] > 15:
                glyph["Refer"][0] = glyph["Refer"][0] + 8

with open('res.json', 'w') as f:
    json.dump(cs, f)