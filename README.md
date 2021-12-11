py-adxl345
==========

Description
-----------

py-adxl345 is a Python driver for ADXL345 chips. ADXL345 chips are
3-axes digital accelerometers from Analog Devices that can communicate
on serial protocols (3/4 wire SPI or 2-wire I2C).

This python driver allows to read 3D acceleration values and 
manage other ADXL345 functions (configuration, fifo, ...).


Requirements
------------

- Require python-smbus to use the I2C protocol
- Require py-spidev to use the SPI protocol


Download
--------

Either download the [zip archive](https://github.com/alexismeneses/py-adxl345/archive/master.zip)

Or clone it using git

    git clone https://github.com/alexismeneses/py-adxl345


Install
-------

Run the following two command

    python setup.py build

    sudo python setup.py install


Usage
-----

You have to use either I2C protocol using adxl345.i2c.ADXL345 class (recommended) or to
use SPI protocol using adxl345.spi.ADXL345 (experimental).

You can find some code usage in [sample](https://github.com/alexismeneses/py-adxl345/tree/master/sample)


More information
----------------

[Constructor website](http://www.analog.com/en/mems-sensors/mems-inertial-sensors/adxl345/products/product.html)


License
-------

Copyright © 2014-2021, Alexis Meneses

This software is licensed under the MIT License (see LICENSE file).
