syntax match space "\."
syntax match clay "#"
syntax match flow "|"
syntax match still "\~"

hi def link space Ignore
hi def link still MatchParen
hi def link flow Type
hi def link clay Conceal

let b:current_syntax = 'day17'

