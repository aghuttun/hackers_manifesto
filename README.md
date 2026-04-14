# Hacker's Manifesto

A Python library written in Rust (PyO3) with three main features:

- Return the full Hacker's Manifesto text.
- Return the Hackers (1995) film-variant excerpt in English.
- Open the original manifesto in the browser: https://phrack.org/issues/7/3

## Exposed Functions

- `get_hackers_manifesto()`
- `get_hackers_manifesto_movie()`
- `open_manifesto_in_browser()`

## Usage in Python

```python
import hackers_manifesto as hm
```

Returns the original Hacker's Manifesto text.

```python
print(hm.get_hackers_manifesto())
```

Returns the Hacker's Manifesto variant featured in the film Hackers.

```python
print(hm.get_hackers_manifesto_movie())
```

Opens your browser to the Phrack page where the original Hacker's Manifesto was published.

```python
hm.open_manifesto_in_browser()
```

## Note

On PyPI/pip, package names are normalised, so `hackers_manifesto` may appear as `hackers-manifesto`. This is expected; the Python import remains `import hackers_manifesto`.
