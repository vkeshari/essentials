# Commands

alias so='source ~/.zshrc'

alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -al'
alias lt='ls -altr'

alias nuke='rm -fR'

# Terminal UI

HISTCONTROL=ignoreboth
setopt histappend

export PS1='%F{yellow}[%n@%m]%f %F{red}%~%f %# '
force_color_prompt=yes

# Languages

alias clang++='clang++ -std=c++20'
alias g++='g++ -std=c++20'

alias python='python3'
alias pip='pip3'

# Mac OS

export PATH=$PATH:/opt/homebrew/bin