**********************************
SQLAlchemy Dialect for SQream DB
**********************************

Requirements
=====================

* Python > 3.9.
* SQLAlchemy == 1.3.18
* SQream Blue DB-API Connector >= 1.0.42

Installation
=====================

Install from the PyPi repository using `pip`:

.. code-block:: bash

    pip3.9 install --upgrade pysqream_blue_sqlalchemy

Usage
===============================

Integrating with SQLAlchemy
----------------------------

.. code-block:: python

    import sqlalchemy as sa
    _access_token = "ACCESS TOKEN"
    conn_str = f"sqream_blue://domain:443/database"
    connect_args = {'access_token': _access_token}
    engine = sa.create_engine(conn_string, connect_args=connect_args)
    conn = engine.connect()
    res = conn.execute("select 'Success' as Test").fetchall()
    print(res)

Integrating with the IPython/Jupyter SQL Magic
-----------------------------------------------

.. code-block:: python

    %load_ext sql
    %config SqlMagic.autocommit=False
    %config SqlMagic.displaycon=False
    %config SqlMagic.autopandas=True
    %sql sqream_blue://product.isqream.com/master?access_token=<ACCESS_TOKEN>
    %sql select 'Success' as Test


Connection String 
=====================

.. code-block:: shell

    sqream_blue://<domain>:443/<db_name>

Parameters
------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``domain``
     - Specifies the domain
   * - ``port``
     - Specifies the port number
   * - ``database``
     - Specifies the database name 


Limitations
=============

Parameterized Queries
-----------------------

SQream SQLAlchemy supports only the ``BULK INSERT`` statement.
