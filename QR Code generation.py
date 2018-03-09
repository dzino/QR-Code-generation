# -*- coding: utf-8 -*-
import imp
import subprocess

class main:

	def __init__(self):
		self.list_lib = [
			'qrcode',
		    'Image'
		]
		self.autoinstallation()

	def autoinstallation(self):
		"""
		check for the presence of the module, if not, the auto-installer starts

		:param list_lib: list of additional libraries
		:type list_lib: dict
		"""
		for lib in self.list_lib:
		    try:
		        imp.find_module(lib)
		        found = True
		        print('OK: Module %s is present in the system'%(lib))
		    except:
		        found = False
		        print('INSTAL: Module %s not found'%(lib))
		        subprocess.call('pip install %s'%(lib), shell=True)

	def generation(self):
		"""
		https://pypi.python.org/pypi/qrcode

		:param inp: custom value
		:type inp: str

		:return img: image
		:type img: obj
		"""
		import qrcode
		while True:
		    self.inpu()
		    qr = qrcode.QRCode(
		        version          = None,
		        error_correction = qrcode.constants.ERROR_CORRECT_L,
		        box_size         = 10,
		        border           = 4,
		    )
		    qr.add_data(self.inp)
		    qr.make(fit=True)
		    self.img = qr.make_image()
		    self.save_file()

	def inpu(self):
		"""
		:return inp: custom value
		:type inp: str
		"""
		try:
			self.inp = input("Enter value:  ")
		except:
			print()
			raise SystemExit

	def save_file(self):
		"""
		:param img: image
		:type img: obj
		"""
		self.img.save('QR-code.png')


if __name__ == '__main__':
	obj = main()
	obj.generation()
