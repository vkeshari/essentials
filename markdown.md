# Markdown Reference

## Formatting

**Bold**

*Italic*

==Highlight==

~~Strikethrough~~

Sub~script~ed

Super^script^ed

## Filenames, commnds, numbers

Contents can be found at `filename.py`.
It has `100` lines of code, the most anyone has ever written.

This is a new line.

## Notes

> :pencil2: **Note:** There is no charge for awesomeness
> :star: **Best Practice:** Don't forget to bring a towel

## Lists

- Best numbers
  - 1
  - 2
    - 2.5
  - 3

1. One
1. Two
  1. Sub-Two
    1. Sub-Sub-Two
  1. Another Sub-Two
1. Three

Always leave a blank line after a list

## Code {#h_code}

Use this one weird trick to speed up your computer `100x`
```
$ sudo rm -Rf /home
```

> :warning: **Warning:** This is a lie. Please **don't** run the command above.

---

Reading between the lines

---

## Some python code

```python
from matplotlib import pyplot as plt

d = {1: 10, 2: 20}
xs, ys = zip(*d.items())
plt.plot(xs, ys, linewidth = 2, alpha = 0.5)
```

> :no_entry_sign: **Deprecated:** This code has now been deprecated. Use package `drawlinefromx1y10tox2y20`.
>> :no_entry_sign: **Deprecated:** Package `drawlinefromx1y10tox2y20` is also deprecated.

## Links

[Dubious source of information](https://google.com)

Go to [Code](#h_code) heading

## Definitions

Indo-gangetic plain
: Vast, fertile, ==densely populated== river basin.
: Most polluted place on Earth[^poullution].
: Birthplace of civilization

[^pollution](https://www.iqair.com/au/india/delhi): New Delhi air pollution
