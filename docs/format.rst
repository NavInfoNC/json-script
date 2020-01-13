JsonScript Format Specification
===============================

.. contents::
   :local:
   :depth: 2

Root Node
---------

'<root>' is used to denote the root of the JSON document. There must be only one root per document.

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

Comments
--------

C++ style comments is used.

Cross Reference in Comments
...........................

Example:

.. code-block:: jss

   <root>
   CatHouse = 
   {
      cats : Cat[]   // also see |Dog| for cross reference.
   }

Types
-----

Internal Types
..............

int
   It can have an integer value. For example 1000.

string
   Quoted string. For example "Hello World".

bool
   It has only two values. "true" or "false".

float
   A real number. It must contain a dot. For example, 1.0

Literal Type
............

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
...........

Enumerations resembles C++ enumerations grammarly.
So it can be copy-pasted between C++ code and JSS document.

Example

.. code-block:: jss

   enum CostModel =
   {
      CostModel_none,      // The value of the first option is 0.
      CostModel_fastest,   // the next one is 1, as in C++
      CostModel_shortest
   }

It's recommended to have a meaningless option as 0.

An enumeration can be used as a value or a string.

1. As value

   .. code-block:: jss

      {
         costModel : CostModel   // as value. It will be stored as int in JSON
      }

   The following JSON document complies with the JSS:

   .. code-block:: js
   
      {
         "costModel" : 2
      }

2. As a string

   .. code-block:: jss

      {
         costModel : CostModel.toString()   // as string. It will be stored as string in JSON.
      }

   The following JSON document complies with the JSS:

   .. code-block:: js
   
      {
         "costModel" : "shortest"
      }

Enumerations can have designated values, as in C++:

.. code-block:: jss

   enum AvoidanceType =
   {
      AvoidanceType_none,
      AvoidanceType_avoidTunnel = 1,   // use designated value to form a bitmap
      AvoidanceType_avoidToll = 2,
      AvoidanceType_avoidExpressway = 4
   }

Class
.....

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

Subclassing
...........

Example:

.. code-block:: jss

   Issue =
   {
      id: int,
      summary: string,
      detail: string,
      reporter: string
   }

   Bug : Issue =
   {
      reproduceSteps: string
   }

   NewFeature : Issue =
   {
      userRequirements: string
   }

Array
.....

Example:

.. code-block:: jss

   {
      speedLimits: int[],
      cats : Cat[]
   }

Advanced Topics
---------------

Inlined Class/Enumeration
.........................

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

Renamed Primitive Types
.......................

By giving a primitive type another name, the document will be easier to understand and more strict.

.. code-block:: jss

   typedef int UnixTimestamp; // Number of seconds since Jan, 1, 1970.
   
   Trip =
   {
      startTime: UnixTimestamp,
      endTime: UnixTimestamp
   }

   typedef int TimeTick;   // the number of milliseconds

   {
      simulationInterval : TimeTick
   }
   
Conditional Field
.................

Some fields only exist when a certain condition is met.

.. code-block:: jss

   {
      variableA : int,
      variableB : string if variableA >= 3 and variableA <= 10
   }

Optional Field
..............

Some fields are ``optional``. If not specified, variables are required by default.

.. code-block:: jss

   {
      variableA : int,              // required (by default)
      variableB : int optional      // optional
      variableC : int required      // required
   }

Constant Value
..............

Constant values are used to express that a symbol must have a specific value.
The equal sign is used to differentiate it from a Literal Type.

.. code-block:: jss

   {
      aString = "HTTP",
      aFloat = 1.0,
      aInt = 1,
      aBool = true
   }
