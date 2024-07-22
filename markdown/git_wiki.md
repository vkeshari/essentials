# GithubWiki-specific Markdown

## Images

### Local Image

[[/path/to/image | Fake image]]

> Note the leading `/` in image path

### HTML Style Image

<image src='path/to/image' alt = 'Fake image' height = 100 width = 100>

## Multi-collapsed sections

<details><summary> View Upper </summary><br>

  > Use spaces around text and a `<br>` after for readability of summary
  
  > Always leave a blank line after `<summary>` block 

  * <details><summary> View Bulleted Inner 1 </summary><br>
      <img src = 'https://images.freeimages.com/vme/images/1/0/107605/peace_sign_clip_art_preview.jpg'>
    </details>
  * <details><summary> View Bulleted Inner 2 </summary><br>
      <img src = 'https://images.freeimages.com/vme/images/1/0/107605/
      peace_sign_clip_art_preview.jpg'>
    </details>
</details>

> Cannot have blank line between bullet points inside `Upper`

> Image doesn't need a blank line after `<summary>` block. All other types (e.g. tables) do need a blank line.

> Do not indent tables inside collapsed block
