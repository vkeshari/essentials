# Markdown Reference

## Formatting

**Bold**

_Italic_

~~Strike~~through

H<sub>2</sub>O

e<sup>-x</sup>

### Extended
```
==Highlight==
```
## Filenames, commnds, numbers

Contents can be found at `filename.py`.
It has `100` lines of code, the most anyone has ever written.

This is a new line.

## Quotes

> There is no charge for awesomeness
>
> .. or attractiveness
> > There is no secret ingredient

## Lists

+ Best numbers
  + 1
  + 2
    + 2.5
  + 3

1. One
   + Two `(located directly below first character)`
     1. Three `(ordered nested in unordered)`
   - Another Two
1. Real Two

Always leave a blank line after a list

## Alerts
> [!NOTE]
> Take note of notes..
>
> .. or be noted.

> [!TIP]
> Choose tip amount:
> + `10%`
> + `20%`
> + `OMG TAKE ALL MY MONEY BECAUSE YOU PRESSED A FEW BUTTONS ON A SCREEN`

## Code

Use this one weird trick to speed up your computer `100x`
```
$ sudo rm -Rf /home
```

> [!IMPORTANT]
> This is a lie. Please don't run the command above.

> [!WARNING]
> For real. **DO NOT** run that command, not even out of curiosity.

---

Read between the lines

---

## Some python code

```python
from matplotlib import pyplot as plt

d = {1: 10, 2: 20}
xs, ys = zip(*d.items())
plt.plot(xs, ys, linewidth = 2, alpha = 0.5)
```

> [!CAUTION]
> **Deprecated:** This code has now been deprecated. Use package `drawlinefromx1y10tox2y20`.

> [!CAUTION]
> **Deprecated:** Package `drawlinefromx1y10tox2y20` is also deprecated now.

## Links

### Extended `{#heading_ref}`

[Dubious source of information](https://google.com)

`Go to [Extended](#heading_ref) heading`

## References

Indo-gangetic plain
+ Vast, fertile, densely populated river basin.
+ Most polluted place on Earth[^1].
+ Birthplace of civilization<sup>\[[citation needed](https://wikipedia.com)\]</sup>

[^1]: (https://www.iqair.com/au/india/delhi): New Delhi air pollution

