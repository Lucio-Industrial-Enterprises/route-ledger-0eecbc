# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in US dollars.

| Parameter   | Values                     | Notes                            |
|-------------|----------------------------|----------------------------------|
| `weight_kg` | positive float             | Parcel weight in kilograms       |
| `zone`      | `"local"`, `"regional"`    | Delivery zone                    |
| `service`   | `"standard"`, `"express"`  | Default `"standard"`; express adds a flat $7 surcharge |

### Python API

```python
from warehouse.rates import shipping_quote

shipping_quote(2, "local")                     # → 8.0  (standard)
shipping_quote(2, "local",  service="express") # → 15.0 (standard + $7)
shipping_quote(2, "regional")                  # → 11.0 (standard)
shipping_quote(2, "regional", service="express") # → 18.0
```

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                   # $8.00
python -m warehouse.cli 2 local --service express # $15.00
```

Unknown zones or services raise `ValueError`; non-positive weights do too.
