# Style Guide
> first of all. we **really** appreciate your attention to contribute into our project!

this is the style guide of our project, here we'll walk you trough how can you write silk looking code that will embed nicely into our code-base

**here is the list of code style guides**

## Code Properties and Formatting
The code should be formatted using [the ruff python formatter](https://github.com/astral-sh/ruff).
Indentation must be 4 **spaces**, Please do not use tabs or less/more than 4 **spaces**

## Defining and Naming
We employ different naming conventions based on use cases:
- `snake_case`: for function or variable definitions.
- `SCREAMING_SNAKE_CASE`: reserved for constants.
- `PascalCase`: employed for class definitions.
- `kebab-case` (`lower-case-only`): utilized for defining a GObject signal/property.

## Comments
Follow [PEP-8's](https://peps.python.org/pep-0008/) guidelines when adding comments. in a nutshell, comments should look:
```python
# Like this.
```
```python
##not like this..##
#nor like this.
#--/ nor whatever else /--#
```

## Logging
Logging should be executed using [loguru](https://github.com/Delgan/loguru). adhere to these rules:
- Be concise; avoid verbosity.
- Refrain from committing files with the log level `debug`.
- Reserve the log level `error` for critical cases, such as severe component failures or dependencies crucial to the entire program.
- Avoid unnecessary `info` statements in low-level classes/modules, unless it's a service subclass.

_If uncertain about where to log, feel free to inquire in the pull request, or someone may suggest a suitable location._

## Conditional Statements
In our code-base we use inline if/else statements if this condition will change the fate of a single object, for example
```python
x = "the x object" if unexcpected_feature is not True else "the x man"
```
and we use normal if statements if that condition will execute a block of code instead of a one line object, here is an example
```python
if unexcpected_feature is True:
    x = "the unknown guy"
    y = "idk"
    z = 4002
```
this choice will be much better than doing
```python
x = "the unknown guy" if unexcpected_feature is True else None
y = "forgor" if unexcpected_feature is True else None
z = 4002 if unexcpected_feature is True else None
```
