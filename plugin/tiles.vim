if !has('python3')
    echomsg ':python3 is not available, vim-find-test will not be loaded.'
    finish
endif

python3 import tiles.tiles
python3 tiles = tiles.tiles.Tiles()

" command! FindTest python3 finder.find()
nnoremap <Leader>e :python3 tiles.vimspector_base_display()<cr>
nnoremap <Leader>f :python3 tiles.vimspector_code_focus()<cr>
nnoremap <Leader>F :python3 tiles.vimspector_code_big_focus()<cr>
nnoremap <Leader>V :python3 tiles.vimspector_variable_focus()<cr>
nnoremap <Leader>S :python3 tiles.vimspector_stack_focus()<cr>

nnoremap <Leader>pp :python3 tiles.show_display()<cr>

