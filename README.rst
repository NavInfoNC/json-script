JsonScript
==========

JsonScript(JSS) is a markup language to describe the structure of JSON file.

Together with Sphinx-Docs_, JSS provides a easy-and-powerful way to describe a JSON file.
It has been widely used in our department to document online service for many years .

A Simple Example
----------------

To document a JSON file:

.. code-block:: js

   {
      "dataVersion" : "NaviInfo.2019.03",
      "routeLength" : 1300.0,
      "eta" : 240
   }

We can use a JSS:

.. code-block:: js

   /* The brief of a route */
   RouteBrief =
   {
      dataVersion : "NaviInfo.2019.03",   // the version of the map data
      routeLength : 1300.0,  // The length of the route, in meters
      eta : int  // Estimated Time of Arrival, in seconds.
   }

As you can see, literal values are often used instead of a types(string, int, float).
And it allows to add C++ style comments.

In This Project
---------------

This project contains:

   * `JSS Format Specification <docs/format.rst>`__
   * `Sphinx Plugin for Syntax hightlight <docs/syntax-highlight-in-sphinx.rst>`__

Notes
-----

JSS's inspired by DataScript_, which is used to describe binary data.

There are other alternatives, like `Json Schema`_.

.. _DataScript: http://datascript.sourceforge.net/
.. _`Json Schema`: https://spacetelescope.github.io/understanding-json-schema/index.html
.. _Sphinx-Docs: http://www.sphinx-doc.org
