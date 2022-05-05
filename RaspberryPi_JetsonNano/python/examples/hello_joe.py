#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import timedelta,datetime
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def wait_until_next_minute():
  end_datetime = (datetime.now()+timedelta(minutes=1)).replace(microsecond=0, second=0)
  while True:
    diff = (end_datetime - datetime.now()).total_seconds()
    # if diff < 0: return       # In case end_datetime was in past to begin with
    time.sleep(diff/2)
    if diff <= 1: return

try:
    epd = epd4in2.EPD()
    logging.info("init and Clear")
    epd.init()
   
    epd.Clear()
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    font80 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 120)

    # Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Himage)

    # draw.text((20, 0), u'Joe!', font = font80)
    # draw.text((20, 155), u'I got this working last night.', font = font18)
    # draw.text((20, 190), u'Make yourself breakfast and do your reading', font = font18)
    # draw.text((100, 240), u'I love you ♡', font = font35)

    while True:
      Himage = Image.open(os.path.join(picdir, 'Bomb.bmp'))
      draw = ImageDraw.Draw(Himage)
      draw.text((10, 282), datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), font = font18)
      

      epd.display(epd.getbuffer(Himage))
      wait_until_next_minute()
      # time.sleep(2)

      
      # draw.text((20, 35), u'微雪电子', font = font35, fill = epd.GRAY2)
      # draw.text((20, 70), u'微雪电子', font = font35, fill = epd.GRAY3)
      # draw.text((40, 110), 'hello world', font = font18, fill = epd.GRAY1)
      # draw.line((10, 140, 60, 190), fill = epd.GRAY1)
      # draw.line((60, 140, 10, 190), fill = epd.GRAY1)
      # draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
      # draw.line((95, 140, 95, 190), fill = epd.GRAY1)
      # draw.line((70, 165, 120, 165), fill = epd.GRAY1)
      # draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
      # draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
      # draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
      epd.display(epd.getbuffer_4Gray(Himage))

      # Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
      # draw = ImageDraw.Draw(Himage)
      # draw.text((10, 0), 'hello world', font = font24, fill = 0)
      # draw.text((10, 20), '4.2inch e-Paper', font = font24, fill = 0)
      # draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
      # draw.line((20, 50, 70, 100), fill = 0)
      # draw.line((70, 50, 20, 100), fill = 0)
      # draw.rectangle((20, 50, 70, 100), outline = 0)
      # draw.line((165, 50, 165, 100), fill = 0)
      # draw.line((140, 75, 190, 75), fill = 0)
      # draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
      # draw.rectangle((80, 50, 130, 100), fill = 0)
      # draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
      # epd.display(epd.getbuffer(Himage))


      logging.info("Goto Sleep...")
      epd.sleep()
      wait_until_next_minute()
    
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2.epdconfig.module_exit()
    exit()
