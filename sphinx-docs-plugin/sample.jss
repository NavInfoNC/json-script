/*
	Some comments
*/
<root>
SomeRootNode = 
{
	formatVersion : string, // some comments
	guid : string,
	length : int,
	size : float,
	enabled : bool
}

SomeType =
{
	formatVersion : "1.0.0",
	guid : "097b1b1b559db449b227bcea36c3bdd3",
	length : 1300
	size : 1.5,
	enabled : true
}

enum CostModel =
{
	CostModel_fastest,
	CostModel_shortest
}

SpeedLimitArray =
{
	speedLimits : int[]
}

CatHouse =
{
	cats : Cat[] // also see `Dog` for cross reference.
}

Cat =
{
	name : string,
	age: int,
	weight: float
}

TypeWithConstantValue =
{
	aString = "HTTP",
	aFloat = 1.0,
	aInt = 1,
	aBool = true
}

TypeWithOptionalField =
{
	variableA : int,
	variableB : string if variableA >= 3
}
