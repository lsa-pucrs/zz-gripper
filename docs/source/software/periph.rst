
=============================================
Hooking Up Peripherals to the Raspberry Pi
=============================================

This section shows how to add the following peripherals to the RPi board

Installing the Raspicam
-----------------------------
The v2 Camera Module has a Sony IMX219 8-megapixel sensor (compared to the 5-megapixel OmniVision OV5647 sensor of the original camera).

 - You can buy the Raspberry Pi Camera Module v2 on oficial website 
	* `oficial website <https://www.raspberrypi.org/products/camera-module-v2/>`_
 - The lab LSA has the camera module V2 `Thisavailable to prototype https://lsa-pucrs.github.io/resources/>`_
 - Power supply is provided by board, you just need to plug
 - The require material is only flat cable to connect the camera into raspberry
 - You need only to enable the camera setup


Installing the ADC - Analog digital converter
-----------------------------

The ADS1115 4-channel digital analog converter is a suitable component for circuits where the microcontroller does not have an ADC (Analog Digital Converter) built-in, or when you need a high-precision converter in your design.

This converter operates with voltages between 2 and 5.5VDC, and the maximum voltage on the analog pins is equal to the supply voltage. Analog pins can be programmed as 4 independent pins, or two differential channels.

The communication interface used by the board is I2C, easy to connect to boards such as Arduino, Raspberry Pi, Beaglebone, etc.

- You can buy the Analog digital converter on 
	* `fillipeflop website <https://www.filipeflop.com/produto/conversor-analogico-digital-4-canais-ads1115/>`_


Installing the ADC sensor
-----------------------------

You just need to :

.. code-block:: bash

    $ sudo pip install adafruit-ads1x15   

