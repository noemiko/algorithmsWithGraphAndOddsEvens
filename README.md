# GraphWithWages
Run this algorithm using example input:
```python
python terrains_analyzer.py
```
Other way write code below:
```python
terrains = TerrainsAnalyzer('path_to_file_with_data')
```

To get smallest terrains travel cost write:
```python
terrains.get_terrains_costs()
```
### example data at file input:
```
2
4, 6
2, 8
3
1, 2, 3
4, 5, 6
7, 8, 9
```

Row with one number represent terrain size.
Rows under the number is terrain with travel cost.

### Run tests 

```python
python -m unittest unit_tests
```

# OddsAndEvenBattle
Run this algorithm using example input:

```python
python war.py
```

Other way write code below:

```python
battlefield_configuration = [randint(-1000, 1000) for _ in range(100)]
war = War()
war.calculate_battle(battlefield_configuration)
```
### Run tests 

```python
python -m unittest unit_tests
```

   
