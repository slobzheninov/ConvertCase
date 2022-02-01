# encoding: utf-8

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from vanilla import Window, Button, Group

class ConvertCase(PalettePlugin):

	def settings( self ):
		self.name = "Convert Case"
		width = 150/3 - 7
		height = 30
		y = 5
		self.paletteView = Window((width, height))
		self.paletteView.group = Group((0, 0, width, height))
		self.paletteView.group.upperCase = Button(( 10, y, width, 15 ), 				"AA", callback=self.buttonCallback )
		setattr( self.paletteView.group.upperCase, 'name', 'upper')
		self.paletteView.group.titleCase = Button(( 10 + width + 7, y, width, 15 ),		"Aa", callback=self.buttonCallback )
		setattr( self.paletteView.group.titleCase, 'name', 'title')
		self.paletteView.group.lowerCase = Button(( 10 + width*2 + 14, y, width, 15 ),  "aa", callback=self.buttonCallback )
		setattr( self.paletteView.group.lowerCase, 'name', 'lower')
		
		# Set dialog to NSView
		self.dialog = self.paletteView.group.getNSView()

	
	@objc.python_method
	def buttonCallback( self, sender ):
		case = sender.name
		if Glyphs.font and Glyphs.font.currentTab and Glyphs.font.currentTab.text:
			tab = Glyphs.font.currentTab

			# change the whole tab if no selection
			if tab.textRange == 0:
				if case == 'upper':
					tab.text = tab.text.upper()
				if case == 'title':
					tab.text = tab.text.title()
				elif case == 'lower':
					tab.text = tab.text.lower()

			# change selected glyphs only
			else:
				selectionStart = tab.textCursor
				selectionEnd = tab.textCursor + tab.textRange
				selectedText = tab.text[ selectionStart : selectionEnd ]

				if case == 'upper':
					tab.text = tab.text[ :selectionStart ] + selectedText.upper() + tab.text[ selectionEnd: ]
				if case == 'title':
					tab.text = tab.text[ :selectionStart ] + selectedText.title() + tab.text[ selectionEnd: ]
				elif case == 'lower':
					tab.text = tab.text[ :selectionStart ] + selectedText.lower() + tab.text[ selectionEnd: ]
			
