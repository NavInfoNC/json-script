JsonScript
==========

JsonScript(JSS) is a markup language to describe the structure of JSON file.

Together with Sphinx-Docs_, JSS provides a easy-and-powerful way to document online service's requests and reponses.
It has been widely used in our department for many years.

A Simple Example
----------------

To document a JSON document:

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

This project contains the design document of JSS and some color-highlight plugins for Sphinx-Docs.

.. toctree::
   :maxdepth: 1

   docs/format
   docs/syntax-highlight-in-sphinx

Notes
-----

JSS's inspired by DataScript_, which is used to describe binary data.

There are other alternatives, like `Json Schema`_.

.. _DataScript: http://datascript.sourceforge.net/
.. _`Json Schema`: https://spacetelescope.github.io/understanding-json-schema/index.html
.. _Sphinx-Docs: http://www.sphinx-doc.org
