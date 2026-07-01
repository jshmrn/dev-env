# export PATH="$HOME/.local/bin:$PATH"
# export PATH="$HOME/Library/Python/3.9/bin:$PATH"
# export PATH="/Applications/WezTerm.app/Contents/MacOS:$PATH"

# file managament
alias la="ls -lah --color=auto"
alias ls="ls --color=auto"
alias ll="ls -lh --color=auto"
alias path='echo -e ${PATH//:/\\n}'
alias codex-install="curl -fsSL https://chatgpt.com/codex/install.sh | sh"

# git shortcut
alias gs="git status"
alias ga="git add"
alias gc="git commit -m"

# config shortcuts
alias esh="nvim ~/.zshrc"
alias rsh="source ~/.zshrc"

# other
source <(fzf --zsh)

