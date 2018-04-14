#!/usr/bin/env python
# coding=utf-8

# Requerimientos:
# - gtts -> pip install gTTS

# Escrito por Alvaro Rodriguez -> https://github.com/AlvaroPelon

from gtts import gTTS
import time
import os
from tempfile import TemporaryFile
from coinmarketcap import Market

class voice:
	def text_to_speech(self, text):
		tts = gTTS(text=text, lang="es")

		testfile = "/tmp/EthereumPrice.mp3"
		tts.save(testfile)

		os.system("mpg123 /tmp/EthereumPrice.mp3")
		os.system("clear")
		os.system("rm %s" %(testfile))

class ethereum:
	def get_price(self, precio=0):
		coinmarketcap = Market()
		eth = coinmarketcap.ticker('ethereum')
		precio = eth[0].get('price_usd')
		return precio[:precio.index('.')]

voice().text_to_speech('El precio del ethereum actualmente es de %s dolares' %(ethereum().get_price()))

