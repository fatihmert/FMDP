#-*- coding: utf-8 -*- 

import Image, struct, pickle, zipfile

def oku(kanal):
        return list(kanal.getdata())
	
def hex2rgb(v):
        v = v.lstrip('#')
        lv = len(v)
        return tuple(int(v[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def rgb2hex(r, g, b):
        return '{:02x}{:02x}{:02x}'.format(r, g, b)
		
		
imj = Image.open('ornek.png','r')

HEX = []
ALF = []

with open("test.fmdp","w") as tt:
	tt.write("fmdp{\n")
	tt.write("\t#[x,y]#HEX-RENK.ALFA#\n")
	if imj.mode in ('RGBA', 'LA') or (imj.mode == 'P' and 'transparency' in imj.info):
			pixels = imj.convert('RGBA').load()
			genis, yuksek = imj.size
			
			for x in range(genis):
					for y in range(yuksek):
						r, g, b, a = pixels[x, y]
						dat = "\t[%s,%s]%s.%s;\n"%(x,y,str(rgb2hex(r, g, b)),str(a))
						tt.write(dat)
	tt.write("}\n")
	with zipfile.ZipFile('test.zip','w',zipfile.ZIP_DEFLATED) as zipp:
		zipp.write('test.fmdp')
