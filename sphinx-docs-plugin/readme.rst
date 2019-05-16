Syntax highlight of DataScript and JsonScript in Sphinx
=======================================================

Prerequisite
------------

   * Python version 2.7.x (https://www.python.org/downloads/)
   * Pygments(Python syntax highlighter)

Installation
------------

* Copy ``jsonscript.py`` into the ``lexers`` directory of the installed Python package: ``pygments``, for example: ``C:\Python27\Lib\site-packages\pygments\lexers``.
* Run ``_mapping.py`` in the ``lexers`` directory to update lexer mapping.

Simple Test
-----------

Run ``pygmentize -O full=True -o sample.html sample.jss`` in the command line, then open ``sample.html`` with your web browser.

Use in Sphinx
-------------

Specify highlighting languages in code block directive, ``jss`` or ``JsonScript`` for JsonScript.

Sample::

   .. code-block:: jss

   /*
      Block comments
   */
   <root>
   SomeRootNode = 
   {
      formatVersion : "1.0.0", // some line comments
      guid : string,
      length : int,
      size : float,
      enabled : bool
   }     

Reference:

   * http://pygments.org/
   * http://pygments.org/docs/lexerdevelopment/

