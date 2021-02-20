# Luby
## _Create a simple restfull service_

Relate Parents with childrens.


## Features

- A parent can have zero to infinity childrens
- A child can have zero to two parents
- Must be in python with postgre database
- Deploy in a docker

## Tables

```sh
CREATE TABLE public.child (
	id serial NOT NULL,
	"name" varchar(150) NOT NULL,
	"CreatedAt" timestamp NULL DEFAULT now(),
	"UpdatedAt" timestamp NULL DEFAULT now(),
	CONSTRAINT child_pkey PRIMARY KEY (id)
);

CREATE TABLE public.parent (
	id serial NOT NULL,
	"name" varchar(150) NOT NULL,
	"CreatedAt" timestamp NULL DEFAULT now(),
	"UpdatedAt" timestamp NULL DEFAULT now(),
	CONSTRAINT parent_pkey PRIMARY KEY (id)
);
```

## Routes

- localhost:5000/api/parent
- localhost:5000/api/parent/{id}
- localhost:5000/api/parents
- localhost:5000/api/child
- localhost:5000/api/child/{id}
- localhost:5000/api/children
- localhost:5000/api/children?parents={NUMBER} return all children with NUMBER of parents
- localhost:5000/api/parents?children={NUMBER} return all parents with NUMBER of children

Specify the relationship between the table during the POST method

## Installation

Install the dependencies and devDependencies and start the ser