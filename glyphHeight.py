font = fontforge.activeFont()
glyphs = font.selection.select(("ranges",None)," ","~").byGlyphs

a_xmin = 0
a_ymin = 0
a_xmax = 0
a_ymax = 0

first = True

for glyph in glyphs:
	(xmin, ymin, xmax, ymax) = glyph.boundingBox()
	if first:
		a_xmin = xmin
		a_ymin = ymin
		a_xmax = xmax
		a_ymax = ymax
		first = False
	else:
		if xmin < a_xmin:
			print(glyph.glyphname)
			
		a_xmin = min(a_xmin, xmin)
		a_ymin = min(a_ymin, ymin)
		a_xmax = max(a_xmax, xmax)
		a_ymax = max(a_ymax, ymax)

print((a_xmin, a_ymin, a_xmax, a_ymax))
