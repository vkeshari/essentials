# Advanced Markdown

## Collapsable Sections

<details>
  <summary> ➕ Expand me </summary>
  
  <br> A line break
  
  This section is a section.
  
  > A quote in the section.

</details>

## Collapsed Image

<details>
  <summary> 🛑 View this image </summary>
  
  ### Stop Sign Image

  ![Stop Sign](https://em-content.zobj.net/thumbs/160/emojidex/85/octagonal-sign_1f6d1.png)
  
</details>

## Collapsed Images with one source outside

<details>
  <summary> 🛑 View this image </summary>
  
  ### Stop Sign Image

  ![Stop Sign][stop]

  ### Another Stop Sign Image

  ![Stop Sign][stop]
  
</details>

[stop]: https://em-content.zobj.net/thumbs/160/emojidex/85/octagonal-sign_1f6d1.png

## Collapsed Collapse

<details>
  <summary> Outer Collapse </summary>

  <br>
  Outer collapse starts here
  
  <details>
    <summary> Inner Collapse </summary>
    <br>
    I am in the inner collapse
    
  </details>
  
  Outer collapse ends here
  
</details>

## Collapsed Table

<details>
  <summary> 📑 View Table </summary>

  | Column | Column |
  | ------ | ------ |
  | Row 1  | Row 1  |
  | ![stop] | ![stop] |
  
</details>
