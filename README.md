# Text expansions

> Note that I recently switched from TextExpander, which has a $36 annual subscription cost, to [espanso](https://espanso.org/), which is free, and, at least in my experience, MUCH faster.
>
> All of the shortcuts below still work, and I have archived the orginal TextExpander backup files in this repo. But the new espanso YAML is available at `default.yml`.
> 
> I have also published a converter to enable you to quickly go from TextExpander to espanso, as I did :)

---


## Clipboard Commands

> Note: These are not yet ported to espanso.

With text selected, use the following commands to replace the text with a modified version:

| Command | Shortcut | Example Before | Example After | Description |
|---------|----------|---------|----------|-----|
| Upper-Case | `\\ku` | `Lorem ipsum` | `LOREM IPSUM` | idk I do this a lot |
| Hyphenate | `\\hyph` | `Lorem ipsum    okay?` | `Lorem-ipsum-okay?` | Great for when you're having a I-need-to-hyphenate-everything sort of day |
| Generate LaTeX | `\\latex` | `x^2` | `http://chart.apis.google.com/chart?cht=tx&chl=x%5E2` (Which is an image that renders as ![](http://chart.apis.google.com/chart?cht=tx&chl=x%5E2) ) | Great for posting formulas in non-LaTeX-friendly systems (like Slack) |
| Italicize (unicode) | `\\textit` | `Are you kidding me?` | `𝑨𝒓𝒆 𝒚𝒐𝒖 𝒌𝒊𝒅𝒅𝒊𝒏𝒈 𝒎𝒆?` | Uses unicode, so may display wonky in some systems |
| Remove line-feeds | `\\non` | `Hello\nworld!` | `Hello world!` | Good for sanitizing your clipboard before pasting into a terminal |

## Arrows

| Symbol | Shortcut |
|--------|----------|
| → | `\rarrow` |
| ← | `\larrow` |
| ↑ | `\uarrow` |
| ↓ | `\darrow` |
| ⟷ | `\lrarrow` |

## Spaces and Dashes

| Symbol | Shortcut |
|--------|----------|
| — | `\--` |
| — | `\mdash` |
| — | `\emdash` |
| – | `\ndash` |
| – | `\endash` |
| [Non-breaking Space] | `\nbsp` |
| [Zero-width Space] | `\zwsp` |
| • | `\bul` |
| ✓ | `\check` |
| [Tab] | `\tabsp` |

## Math

| Symbol | Shortcut |
|--------|----------|
| × | `\times` |
| ⊂ | `\subset` |
| μ | `\mu` |
| ± | `\pm` |
| ∫ | `\int` |
| ∞ | `\inf` |
| ∑ | `\sum` |
| ϴ | `\Theta` |
| ∈ | `\setin` |
| ∆ | `\Delta` |
| º | `\deg` |
| ∩ | `\cap` |
| ∪ | `\cup` |
| ≤ | `\leq` |
| ≥ | `\geq` |
| β | `\beta` |
| ≈ | `\approx` |
| Ξ | `E-\|` |
| ∀ | `\forall` |

## Numerals 

| Symbol | Shortcut |
|--------|----------|
| ① | `\(1)` |
| ② | `\(2)` |
| ③ | `\(3)` |
| ④ | `\(4)` |

## Pinyin

**Mnemonic:** All pinyin vowels (including ü) are supported. Type the vowel, and then type the vertical bar (<kbd>|</kbd>) and while holding shift, press the tone (1,2,3,4). In other words, to type `ú`, type <kbd>u</kbd> and then <kbd>|</kbd><kbd>@</kbd> (because `@` is Shift+2, for 2nd-tone). To type `ü` vowels, use `u:` in place of the vowel. For example, `ǘ` is `u|:@`. 

| Symbol | Shortcut |
|--------|----------|
| ā | `a\|!` |
| á | `a\|@` |
| ǎ | `a\|#` |
| à | `a\|$` |
| etc. |
