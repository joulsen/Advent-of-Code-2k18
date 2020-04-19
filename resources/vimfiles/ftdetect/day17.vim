autocmd BufRead,BufNewFile *.day17 set filetype=day17
:set wrap!
:vmap <C-S> :s/\%V\./\~/g<CR>
:vmap <C-F> :s/\%V\./\|/g<CR>
:map <C-L> zL
:map <C-H> zH
