from distutils.core import setup
import py2exe

setup(windows=['DataMigrationTool.pyw'],
      options={'py2exep' : {'packages':['Tkinter']}})
