
=============================================
Installing the OS
=============================================

The OS version used on Raspberry Pi 3 is Ubuntu MATE 16.04.2.
The ROS version is Kinetic Kame. Kinetic was released early last year and is compatible with `Ubuntu Mate 16.04 <https://ubuntu-mate.org/raspberry-pi/>`_.


Pre Built Image
--------------------

There is a prebuilt image with Ubuntu MATE 16.04.2 and ROS Kinetic at the `German Robot webpage <http://www.german-robot.com/2016/05/26/raspberry-pi-sd-card-image/>`_, made in February 2017. This is the fastest way to get the job done.


Prepare yourself the Image
--------------------

If you want to do it yourself, then follow these steps:

- Download `Ubuntu Mate image <https://ubuntu-mate.org/download/>`_ for raspiberry 2/3 - Version 16.04 (Xenial)
- Use `Etcher <https://etcher.io/>` or `Win32 Disk Imager <https://sourceforge.net/projects/win32diskimager/>` _ to burn the image to the SD card.
- how to the partitioning (to be completed)
- you might need to resize the image if your disk is larger then 8GB. You can easily do it with ``raspi-config`` or ``gparted``.
- plug the SD card and HDMI cable, then power on the board.

Setting Up the OS
--------------------

It might be required to setup the OS (TO BE DONE)

- which basics packages to install
- how to setup the wireless
- main depedencies to intall
- setup automatic login
- how to enable the rpi pins and protocols (i2c, gpio, pwm, spi,camera  etc)


Image is ready ! let's install ROS!
