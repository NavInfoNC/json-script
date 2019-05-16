JsonScript Format Specification
===============================

.. contents::
   :local:
   :depth: 2

Root Node
---------

'<root>' is used to denote the root of the json document. There must be only one root per document.

.. code-block:: jss

   /*
      Some comments
   */
   <root>
   SomeRootNode = 
   {
      variableName1: Type1,   // some comments
      variableName2: Type2,
      ...
   }

Types
-----

Internal Types
^^^^^^^^^^^^^^

   int
      Can have integer value. For example 1000.

   string
      Quoted string. For example "Hello World".

   bool
      It have have only two values. "true" or "false".

   float
      It must contain a dot. For example, 1.0

Literal Type
^^^^^^^^^^^^

   To provide insights into the value of a string or number,
   literal types can be used in place of regular types.

   For example, the following two expressions are equivalent:

   .. code-block:: jss
   
      {
         formatVersion : string,
         guid : string,
         length : int,
         size : float,
         enabled : bool
      }

      {
         formatVersion : "1.0.0",
         guid : "097b1b1b559db449b227bcea36c3bdd3",
         length : 1300
         size : 1.5,
         enabled : true
      }

Enumeration
^^^^^^^^^^^

Enumerations resembles C++ enumerations grammarly.
So it can be copy-pasted between C++ code and JSS document.

Example

.. code-block:: jss

   enum CostModel =
   {
      CostModel_none,      // The value of the first option is 0.
      CostModel_fastest,   // the next one is 1
      CostModel_shortest
   }

It's recommended to have a meaningless option as 0.

A enumeration can be used as value, or as string.

   1. As value

      .. code-block:: jss

         {
            costModel : CostModel   // as value. It will be stored as int in JSON
         }

      The following JSON document comply with the JSS:

      .. code-block:: js
      
         {
            "costModel" : 2
         }

   2. As string

      .. code-block:: jss

         {
            costModel : CostModel.toString()   // as string. It will be stored as string in JSON.
         }

      The following JSON document comply with the JSS:

      .. code-block:: js
      
         {
            "costModel" : "shortest"
         }

Enumerations can have designated value, as in C++:

.. code-block:: jss

   enum AvoidanceType =
   {
      AvoidanceType_none,
      AvoidanceType_avoidTunnel = 1,   // use designated value to form a bitmap
      AvoidanceType_avoidToll = 2,
      AvoidanceType_avoidExpressway = 4
   }

Class
^^^^^

Example:

.. code-block:: jss

   <root>
   CatHouse = 
   {
      cats : Cat[]
   }

   Cat = 
   {
      name : string,
      age: int,
      weight: float
   }

Inlined Class/Enumeration
^^^^^^^^^^^^^^^^^^^^^^^^^

If a class or enumeration only appears in one place, it can be inlined or even unnamed.

Exmaple:

.. code-block:: jss

   CatHouse = 
   {
      type : CatHouseType { // an inlined enumeration
         CatHouseType_none,
         CatHouseType_luxurious,
         CatHouseType_minimalism
      }

      windows : Window[] { // an inlined class
         width : int,
         height : int
      },

      cats : [] {       // an inlined and unamed class
         name : string,
         age: int,
         weight: float
      }
   }
   
Array
^^^^^

Example

.. code-block:: jss

   {
      speedLimits: int[],
      cats : Cat[]
   }

Constant Value
--------------

Constant values are used to express that a symbol must have the specified value.
The equal sign is used to differentiate it from a Literal Type.

.. code-block:: jss

   {
      aString = "HTTP",
      aFloat = 1.0,
      aInt = 1,
      aBool = true
   }

Comments
--------

C++ style comments is used.

Cross Reference in Comments
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example:

.. code-block:: jss

   <root>
   CatHouse = 
   {
      cats : Cat[]   // also see `Dog` for cross reference.
   }

Optinal Field
-------------

Some fields only exist when certain condition is met.

.. code-block:: jss

   {
      variableA : int,
      variableB : string if variableA >= 3 and variableA <= 10
   }
