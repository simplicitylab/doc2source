# Database documentation

## Car 

* name (string)
* description (string, nullable=true, size=255)
* price (int)
* color (string)
* hotrod (boolean)
* number of wheels (int)
* brand -> Brand
* suppliers <-> Supplier

## Brand
* name (string)

## Supplier
* name (string)
