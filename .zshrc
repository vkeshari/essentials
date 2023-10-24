
alias so='source ~/.zshrc'

alias ls='ls --color=auto'
alias ll='ls -al'
alias lt='ls -altr'

alias nuke='rm -fR'

HISTCONTROL=ignoreboth
setopt histappend

export PS1='%F{yellow}[%n@%m]%f %F{red}%~%f %# '
force_color_prompt=yes
